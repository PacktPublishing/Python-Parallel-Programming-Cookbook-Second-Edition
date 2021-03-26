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

    #def test_02_alif_1184068(self):
    #    from Chapter02.Alif1184068 import main	
    #    response = 	main()
    #    self.assertEqual(response, True)

    #def test_02_iradwita_1184024(self):
    #    from Chapter02.IraDwita1184024 import main	
    #    response = 	main()
    #    self.assertEqual(response, True)
        
    #def test_02_bahar_1184002(self):
    #    from Chapter02.baharandili1184002 import main  
    #    response =  main()
    #    self.assertEqual(response, True)

    #def test_02_hanif_1184058(self):
    #    from Chapter02.Hanif1184058 import main    
    #    response =  main()
    #    self.assertEqual(response, True)
        
    #def test_02_parhan_1184042(self):
    #    from Chapter02.Parhan1184042 import main    
    #    response =  main()
    #    self.assertEqual(response, True)
    def test_02_ravi_1184040(self):
         from Chapter02.Ravi1184040 import main    
         response =  main()
         self.assertEqual(response, True)
    
    def readfile(self,nfile):
        f = open(nfile, "r+")
        #f.read(20)
        return str(f.read())	
       
    def test_03_raviDua1184050(self):
        from Chapter02.raviDua1184040 import raviDua1184040,raviSemaphorewriteFile
        threadwrite= raviSemaphorewriteFile("Thread write File ", 1,'nilai')
        threadutama = raviDua1184040("Thread Utama ", 2,2,5,'nilai')
        threadwrite.start()
        threadutama.start()
        threadwrite.join()
        threadutama.join()
        respon=self.readfile('./Chapter02/nilai.html')
        self.assertRegex(respon, "Nomor : 12345678910")
    
#    def readfile(self,filename):
#        f = open(filename, "r")
#        return int(f.read())	
       
#    def test_03_zanwarDua1184050(self):
#        from Chapter02.ZanwarDua1184050 import zanwarDua1184050,zanwarRewrite
#        threadrewrite= zanwarRewrite("Thread Rewrite File ", 1,'nilai')
#        threadutama = zanwarDua1184050("Thread Utama ", 2,2,5,'nilai')
#        threadrewrite.start()
#        threadutama.start()
#        threadrewrite.join()
#        threadutama.join()
#        respon=self.readfile('./Chapter02/nilai.txt')
#        self.assertGreaterEqual(respon, 0)
    
    
    
    
    
    
    
