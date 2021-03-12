import unittest
import json
import os

from app import app

from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager

from module import absensi_karyawan

class TestITeung(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

        self.jwt = JWTManager(app)

    def tearDown(self):
        pass

    def test_00_register_karyawan(self):
        data_json = {
            "data_user": {
                "idKaryawan": "118.40.047",
                "passwordKaryawan": "123"
            },
            "data_device": {
                "deviceId": "unknown",
                "deviceType": "Handset",
                "macAddress": "6C:D7:1F:29:C9:11",
                "uniqueId": "11c5a2b8030b2033",
                "isEmulator": "false"
            },
            "data_alamat": {
                "namaJalan": "Jl. Testing",
                "nomorRt": "010",
                "nomorRw": "008",
                "namaKelurahan": "SARIJADI",
                "namaKecamatan": "SUKASARI",
                "namaKota": "KOTA BANDUNG",
                "namaProvinsi": "PROV. JAWA BARAT",
                "kodeKelurahan": "32.73.01.1004"
            }
        }
        response = self.app.post('/api/v1/daftar/karyawan', json=data_json)
        self.assertEqual(response.status_code, 200)

    def test_01_get_nik_nama(self):
        response = self.app.get('/api/v1/nik_nama/karyawan', headers=[('API-Key', 'trianggadio@gmail.com')])
        self.assertEqual(response.status_code, 200)

    def test_02_login_android_karyawan(self):
        data_json = {
            "username": "118.40.047",
            "password": "123",
            "data_device": {
                "deviceId": "unknown",
                "deviceType": "Handset",
                "macAddress": "6C:D7:1F:29:C9:11",
                "uniqueId": "11c5a2b8030b2033",
                "isEmulator": "false"
            }
        }
        response = self.app.post('/android/api/login', json=data_json)
        data = json.loads(response.data)
        os.environ["JWT_TOKEN_ACCESS"] = data['access_token']
        os.environ["JWT_REFRESH_ACCESS"] = data['refresh_token']
        self.assertEqual(response.status_code, 200)

    def test_03_logout_android_karyawan(self):
        headers = {
            'Authorization': "Bearer {}".format(os.environ["JWT_TOKEN_ACCESS"])
        }
        response = self.app.post('/android/api/logout', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_04_refresh_jwt_token(self):
        headers = {
            'Authorization': "Bearer {}".format(os.environ["JWT_REFRESH_ACCESS"])
        }
        response = self.app.post('/refresh/token/jwt', headers=headers)
        os.environ["JWT_TOKEN_ACCESS"] = json.loads(response.data)['access_token']
        self.assertEqual(response.status_code, 200)

    def test_05_get_alamat_karyawan(self):
        headers = {
            'Authorization': "Bearer {}".format(os.environ["JWT_TOKEN_ACCESS"])
        }
        response = self.app.get('/api/v1/alamat/karyawan', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_06_daftar_alamat(self):
        response = self.app.get('/api/v1/daftar/alamat')
        self.assertEqual(response.status_code, 200)

    def test_07_nik_nama_karyawan(self):
        response = self.app.get('/api/v1/nik_nama/karyawan', headers=[('API-Key', 'trianggadio@gmail.com')])
        self.assertEqual(response.status_code, 200)

    def test_08_absensi_karyawan(self):
        headers = {
            'Authorization': "Bearer {}".format(os.environ["JWT_TOKEN_ACCESS"])
        }
        data_json = {
            "latitude": "-6.8080",
            "longitude": "107.12345",
            "status_location": "rumah",
            "data_device": {
                "deviceId": "unknown",
                "deviceType": "Handset",
                "macAddress": "6C:D7:1F:29:C9:11",
                "uniqueId": "11c5a2b8030b2033",
                "isEmulator": "false"
            }
        }
        response = self.app.post('/api/v1/absensi/karyawan', headers=headers, json=data_json)
        self.assertEqual(response.status_code, 200)

    def test_09_lat_lng_karyawan_data(self):
        data_json = {
            "kode_kelurahan": "32.73.01.1004"
        }
        response = self.app.post('/api/v1/lat_lng/kelurahan/karyawan', json=data_json, headers=[('API-Key', 'trianggadio@gmail.com')])
        self.assertEqual(response.status_code, 200)

    def test_10_kehadiran_karyawan(self):
        data_json = {
            "id_karyawan": "118.40.047",
            "hari_awal": "2020-01-01",
            "hari_akhir": "2020-01-25"
        }
        response = self.app.post('/api/v1/kehadiran/karyawan', json=data_json, headers=[('API-Key', 'trianggadio@gmail.com')])
        self.assertEqual(response.status_code, 200)

    def test_11_emulator_testing_true(self):
        data_json = {
            "username": "118.40.047",
            "password": "123",
            "data_device": {
                "deviceId": "unknown",
                "deviceType": "Handset",
                "macAddress": "6C:D7:1F:29:C9:11",
                "uniqueId": "11c5a2b8030b2033",
                "isEmulator": "true"
            }
        }
        response = self.app.post('/android/api/login', json=data_json)
        self.assertEqual(response.status_code, 403)

    def test_12_missing_emulator_param(self):
        data_json = {
            "username": "118.40.047",
            "password": "123",
            "data_device": {
                "deviceId": "unknown",
                "deviceType": "Handset",
                "macAddress": "6C:D7:1F:29:C9:11",
                "uniqueId": "11c5a2b8030b2033"
            }
        }
        response = self.app.post('/android/api/login', json=data_json)
        self.assertEqual(response.status_code, 400)

    def test_13_missing_data_device_param(self):
        data_json = {
            "username": "118.40.047",
            "password": "123"
        }
        response = self.app.post('/android/api/login', json=data_json)
        self.assertEqual(response.status_code, 400)

    def test_14_not_secretary_email(self):
        response = self.app.get('/api/v1/nik_nama/karyawan', headers=[('API-Key', 'iteung@gmail.com')])
        self.assertEqual(response.status_code, 401)

    def test_15_wrong_username_or_password(self):
        data_json = {
            "username": "118.40.099",
            "password": "123",
            "data_device": {
                "deviceId": "unknown",
                "deviceType": "Handset",
                "macAddress": "6C:D7:1F:29:C9:11",
                "uniqueId": "11c5a2b8030b2033",
                "isEmulator": "false"
            }
        }
        response = self.app.post('/android/api/login', json=data_json)
        self.assertEqual(response.status_code, 401)

    def test_16_false_logout(self):
        session_id = absensi_karyawan.create_session_id()
        with app.test_request_context():
            access_token = create_access_token(identity=session_id)
        headers = {
            'Authorization': "Bearer {}".format(access_token)
        }
        response = self.app.post('/android/api/logout', headers=headers)
        self.assertEqual(response.status_code, 401)