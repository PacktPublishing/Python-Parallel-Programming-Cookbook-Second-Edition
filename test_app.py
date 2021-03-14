import unittest



from Chapter01 import serial_test,multiprocessing_test,multithreading_test


class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_00_serial(self):
        response = serial_test.serial_test()
        self.assertEqual(response, True)

    def test_01_multithreading(self):
        response = multithreading_test.multithreading_test()
        self.assertEqual(response, True)

    def test_02_multiprocessing(self):
        response = multiprocessing_test.multiprocessing_test()
        self.assertEqual(response, True)
		
    def test_03_rolly_113040087(self):
        from Chapter02.Rolly113040087 import main	
        response = 	main()
        self.assertEqual(response, True)
		
