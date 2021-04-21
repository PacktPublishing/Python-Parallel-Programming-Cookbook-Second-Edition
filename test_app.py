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
    

    def readfile(self,filename):
        f = open(filename, "r")
        return str(f.read())
        f.close()	

       
    # def test_07_zanwarTujuh1184050(self):
    #     from Chapter02.ZanwarTujuh1184050 import zanwarTujuh1184050, zanwarRewrite
    #     thread1 = zanwarRewrite("Thread Rewrite File ",1 , 'nilai')
    #     thread2 = zanwarTujuh1184050("Thread Utama ", 2, 5, 'nilai')
    #     thread2.start()
    #     thread1.start()
    #     thread2.join()
    #     thread1.join()
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

    # def test_06_Ferdy_1184112(self):
    #     from Chapter02.FerdyEnam1184112 import main
    #     response =  main()
    #     self.assertEqual(response, True)

    # def test_06_josuansef_1184091(self):
    #      from Chapter02.JosuansefEnam_1184091 import main
    #      response =  main()
    #      self.assertEqual(response, True)

#    def test_03_FerdyEvent1184112(self):
#       from Chapter02.FerdyTujuh1184112 import FerdyQueue,Ferdy
#       threadjuga= FerdyQueue("Thread Lain ",'queue')
#       threadaja = Ferdy("Thread inti",'queue')
#       threadjuga.start()
#       threadaja.start()
#       threadjuga.join()
#       threadaja.join()
#       respon=self.readfile('./Chapter02/queue')
#       self.assertNotRegex(respon, "Gak Boleh Kosong")

    # def test_07_HernandezTujuh1184014(self):
        # from Chapter02.IrfanHernandezTujuh1184014 import IrfanPut
        # thread1 = IrfanPut("Thread Put", 1, "miramas")
        # thread1.start()
        # thread1.join()
        # respon=self.readfile('./Chapter02/miramas.txt')
        # self.assertNotRegex(respon, "Kosong")
    
    
    # def test_07_alifTujuh1184068(self):
        # from Chapter02.AlifTujuh1184068 import alifTujuh1184068,alifHandlingFile  
        # threadutama = alifTujuh1184068("Thread Utama ", 2,5,5,'alip')
        # threadhandling= alifHandlingFile("Thread handling File ", 1,'alip')
        # threadhandling.start()
        # threadutama.start()
        # threadhandling.join()
        # threadutama.join()
        # respon=self.readfile('./Chapter02/alip.txt')
        # self.assertNotRegex(respon, "kosong")
		
	def test_07_AnisaTujuh1184016(self):
        from Chapter02.AnisaRosalinaTujuh1184016 import Anisa
        thread1 = Anisa("Thread Put", 1, "Cocktile")
        thread1.start()
        thread1.join()
        respon=self.readfile('./Chapter02/Cocktile.txt')
        self.assertNotRegex(respon, "Kosong")
    