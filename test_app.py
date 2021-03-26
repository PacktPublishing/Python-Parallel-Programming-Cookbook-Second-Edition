import unittest



#from Chapter01 import serial_test,multiprocessing_test,multithreading_test


class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

#    def test_00_serial(self):
#        response = serial_test.serial_test()
#        self.assertEqual(response, True)
#
#    def test_01_multithreading(self):
#        response = multithreading_test.multithreading_test()
#        self.assertEqual(response, True)
#
#    def test_02_multiprocessing(self):
#        response = multiprocessing_test.multiprocessing_test()
#        self.assertEqual(response, True)
		
<<<<<<< HEAD
    # def test_02_kaisar_1184093(self):
    #     from Chapter02.Kaisar1184093 import main	
    #     response = 	main()
    #     self.assertEqual(response, True)
    
    # def test_02_rizaluardi_1184102(self):
    #     from Chapter02.Rizaluardi1184102 import main
    #     response =  main()
    #     self.assertEqual(response, True)
        
    # def test_02_zanwar_1184050(self):
    #     from Chapter02.Zanwar1184050 import main
    #     response =  main()
    #     self.assertEqual(response, True)
        
    #def test_02_ferdy_1184112(self):
    #   from Chapter02.Ferdy1184112 import main
    #  response = main()
    # self.assertEqual(response, True)

    #def test_02_ida_1184113(self):
    #   from Chapter02.Ida1184113 import main
    #    response = main()
    #    self.assertEqual(response, True)

    #def test_02_okky_1184087(self):
    #    from Chapter02.okky1184087 import main
    #    response = main()
    #    self.assertEqual(response, True)
    
    
    #def test_02_Nandez_1184014(self):
    #    from Chapter02.IrfanHernandez1184014 import main
    #    response = main()
     #   self.assertEqual(response, True)
     
    def test_02_josua_1184091(self):
        from Chapter02.josua_1184091 import main    
        response =  main()
        self.assertEqual(response, True)
=======
    def test_02_rolly_113040087(self):
        from Chapter02.Rolly113040087 import main	
        response = 	main()
        self.assertEqual(response, True)
        
    def readfile(self,namafile):
        f = open(namafile, "r")
        return int(f.read())	
       
    def test_03_rollyDua113040087(self):
        from Chapter02.rollyDua113040087 import rollyDua113040087,rollySemaphoreDeleteFile
        threaddelete= rollySemaphoreDeleteFile("Thread Delete File ", 1,'anu')
        threadutama = rollyDua113040087("Thread Utama ", 2,5,5,'anu')
        threaddelete.start()
        threadutama.start()
        threaddelete.join()
        threadutama.join()
        respon=self.readfile('./Chapter02/anu.croot')
        self.assertGreaterEqual(respon, 0)
        
        
>>>>>>> a6ae71262e263e401dde92eb13edffb6399aaf2c
