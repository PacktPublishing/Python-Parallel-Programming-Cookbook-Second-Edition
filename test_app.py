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
    

    # def readfile(self,filename):
    #     f = open(filename, "r")
    #     return str(f.read())	

    # def readfile(self,filename):
    #     f = open(filename, "r")
    #     return str(f.read())	

       
    # def test_03_zanwarTiga1184050(self):
    #     from Chapter02.ZanwarTiga1184050 import zanwarTiga1184050, zanwarRewrite
    #     threadrewrite= zanwarRewrite("Thread Rewrite File ",1 , 'nilai')
    #     threadutama = zanwarTiga1184050("Thread Utama ", 2, 1, 'nilai')
    #     threadrewrite.start()
    #     threadutama.start()
    #     threadrewrite.join()
    #     threadutama.join()
    #     respon=self.readfile('./Chapter02/nilai.txt')
    #     self.assertNotRegex(respon, "Kosong")
    
#    def test_03_WahyuKurniaSariDua1184001(self):
 #       from Chapter02.WahyuKurniasariDua1184001 import WahyuKurniaSariSemaphoreDeleteFile,  WahyuKurniaSariDua1184001
  #      delete = WahyuKurniaSariSemaphoreDeleteFile("Thread delete", 1,"pikachu")
   #     main =  WahyuKurniaSariDua1184001("Thread utama", 2,"pikachu", "pikachu") 
    #    delete.start()
     #   main.start()
      #  delete.join()
       # main.join()
        #self.assertGreaterEqual(main.getFileContent(),0 )

    # def test_03_alifTiga1184068(self):
    #     from Chapter02.alifTiga1184068 import alifTiga1184068,alifEventDeleteFile  
    #     threadutama = alifTiga1184068("Thread Utama ", 2,5,5,'alip')
    #     threaddelete= alifEventDeleteFile("Thread Delete File ", 1,'alip')
    #     threaddelete.start()
    #     threadutama.start()
    #     threaddelete.join()
    #     threadutama.join()
    #     respon=self.readfile('./Chapter02/alip.txt')
    #     self.assertNotRegex(respon, "kosong")



    # def test_03_FerdyTiga1184112(self):
    #     from Chapter02.FerdyTiga1184112 import FerdyGITiga1184112,FerdyEventGI
    #     threadrewrite= FerdyEventGI("Thread Lain ", 1,'minuman')
    #     threadutama = FerdyGITiga1184112("Thread inti ", 2,'minuman')
    #     threadrewrite.start()
    #     threadutama.start()
    #     threadrewrite.join()
    #     threadutama.join()
    #     respon=self.readfile('./Chapter02/minuman.txt')
    #     self.assertNotRegex(respon, "Gak Boleh Kosong")
	
    # def test_03_hanifTiga1184058(self):
    #     from Chapter02.HanifTiga1184058 import hanifTiga1184058, hanifRename
    #     threadrename= hanifRename("Thread rename file ",1 , 'nilai')
    #     threadutama = hanifTiga1184058("Thread utama ", 2, 1, 'nilai')
    #     threadrename.start()
    #     threadutama.start()
    #     threadrename.join()
    #     threadutama.join()
    #     respon=self.readfile('./nilai.txt')
    #     self.assertNotRegex(respon, "Kosong")
    # def readfile(self,nfile):
    #     f = open(nfile, "r+")
    #     return str(f.read())	
       
       
    # def test_03_raviTiga1184040(self):
    #     from Chapter02.raviTiga1184040 import raviTiga1184040, raviMenulis 
    #     threadwrite = raviMenulis ("Thread Pro ",1 , 'value')
    #     threadutama = raviTiga1184040("Thread Utama ", 2,2,5, 'value')
    #     threadwrite.start()

    # def test_03_FerdyTiga1184112(self):
    #     from Chapter02.FerdyTiga1184112 import FerdyGITiga1184112,FerdyEventGI
    #     threadrewrite= FerdyEventGI("Thread Lain ", 1,'minuman')
    #     threadutama = FerdyGITiga1184112("Thread inti ", 2,'minuman')
    #     threadrewrite.start()

    #     threadutama.start()
    #     threadwrite.join()
    #     threadutama.join()

    #     respon=self.readfile('./Chapter02/value.pdf')
    #     self.assertNotRegex(respon, "Nomor :  12345678910")

    #     respon=self.readfile('./Chapter02/minuman.txt')
    #     self.assertNotRegex(respon, "Gak Boleh Kosong")
	
    # def test_03_hanifTiga1184058(self):
    #     from Chapter02.HanifTiga1184058 import hanifTiga1184058, hanifRename
    #     threadrename= hanifRename("Thread rename file ",1 , 'nilai')
    #     threadutama = hanifTiga1184058("Thread utama ", 2, 1, 'nilai')
    #     threadrename.start()
    #     threadutama.start()
    #     threadrename.join()
    #     threadutama.join()
    #     respon=self.readfile('./nilai.txt')
    #     self.assertNotRegex(respon, "Kosong")
    #
    def readfile(self,nfile):
        f = open(nfile, "r+")
        return str(f.read())	
       
    # def test_03_raviTiga1184040(self):
    #     from Chapter02.raviTiga1184040 import raviTiga1184040, raviMenulis 
    #     threadwrite = raviMenulis ("Thread Pro ",1 , 'value')
    #     threadutama = raviTiga1184040("Thread Utama ", 2,2,5, 'value')
    #     threadwrite.start()
    #     threadutama.start()
    #     threadwrite.join()
    #     threadutama.join()
    #     respon=self.readfile('./Chapter02/value.pdf')
    #     self.assertNotRegex(respon, "Nomor :  12345678910")

    # def test_03_parhanTiga1184042(self):
    #     from Chapter02.parhanTiga1184042 import parhanTiga1184042,parhanEventDeleteFile  
    #     threadutama = parhanTiga1184042("Thread Utama ", 2,5,5,'parhan')
    #     threaddelete= parhanEventDeleteFile("Thread Delete File ", 1,'parhan')
    #     threaddelete.start()
    #     threadutama.start()
    #     threaddelete.join()
    #     threadutama.join()
    #     respon=self.readfile('./Chapter02/parhan.txt')
    #     self.assertNotRegex(respon, "kosong")

    # def test_06_Ferdy_1184112(self):
    #     from Chapter02.FerdyEnam1184112 import main
    #     response =  main()
    #     self.assertEqual(response, True)

    # def test_06_zanwar_1184050(self):
    #     from Chapter02.ZanwarEnam1184050 import main
    #     response =  main()
    #     self.assertEqual(response, True)
    
    #def test_06_alif_1184068(self):
    #    from Chapter02.AlifEnam1184068 import main
    #    response =  main()
    #    self.assertEqual(response, True)
    
    # def test_06_parhan_1184042(self):
    #     from Chapter02.ParhanEnam1184042 import main
    #     response =  main()
    #     self.assertEqual(response, True)

    def test_06_ida_1184113(self):
        from Chapter02.IdaEnam1184113 import main
        response =  main()
        self.assertEqual(response, True)