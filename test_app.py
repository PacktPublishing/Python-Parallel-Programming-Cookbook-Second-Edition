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


#    def test_03_parhanTiga1184042(self):
#        from Chapter02.parhanTiga1184042 import parhanTiga1184042,parhanEventDeleteFile  
#        threadutama = parhanTiga1184042("Thread Utama ", 2,5,5,'parhan')
#        threaddelete= parhanEventDeleteFile("Thread Delete File ", 1,'parhan')
#        threaddelete.start()
#        threadutama.start()
#        threaddelete.join()
#        threadutama.join()
#        respon=self.readfile('./Chapter02/parhan.txt')
#        self.assertNotRegex(respon, "kosong")
#        
#    def test_03_okkyTiga1184087(self):
#        from chapter02.okkyTiga1184087 import okky1184087Write_Trier, okky1184087
#        threadwrite = okky1184087Write_Trier ("Thread satu ",1 , 'okky1')
#        threadutama = okky1184087("Thread dua ", 2,2, 'okky2')
#        threadwrite.start()
#        threadutama.start()
#        threadwrite.join()
#        threadutama.join()
#        respon=self.readfile('./Chapter02/value.pdf')
#        self.assertNotRegex(respon, "Nomor :  12345678910")

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


   # def test_06_parhan_1184042(self):
        #from Chapter02.ParhanEnam1184042 import main
        #response =  main()
        #self.assertEqual(response, True)

    #def test_06_ira_1184024(self):
        #from Chapter02.IraEnam1184024 import main
        #response =  main()
        #self.assertEqual(response, True)


    #def test_06_parhan_1184042(self):
    #    from Chapter02.ParhanEnam1184042 import main
    #    response =  main()
    #    self.assertEqual(response, True)


    # def test_06_hanif_1184058(self):
    #     from Chapter02.HanifEnam1184058 import main
    #     response =  main()
    #     self.assertEqual(response, True)


    #def test_06_WahyuKurniaSari_1184001(self):


      # def test_06_WahyuKurniaSari_1184001(self):
    #     from Chapter02.WahyuKurniaSariEnam1184001 import main
    #     result=main()
    #     self.assertEqual(result, True)

   
    #def test_06_WahyuKurniaSari_1184001(self):

        #from Chapter02.WahyuKurniaSariEnam1184001 import main
        #result=main()
        #self.assertEqual(result, True)

    # def test_06_ira_1184024(self):
    #     from Chapter02.IraEnam1184024 import main
    #     response =  main()
    #     self.assertEqual(response, True)



    #    from Chapter02.WahyuKurniaSariEnam1184001 import main
    #    result=main()
    #    self.assertEqual(result, True)

    #def test_06_ira_1184024(self):
    #    from Chapter02.IraEnam1184024 import main
    #    response =  main()
    #    self.assertEqual(response, True)


    # def test_06_rizaluardi_1184102(self):
    #     from Chapter02.RizaluardiEnam1184102 import main
    #     result=main()
    #     self.assertEqual(result, True)

    #def test_06_rizaluardi_1184102(self):
    #    from Chapter02.RizaluardiEnam1184102 import main
    #    result=main()
    #    self.assertEqual(result, True)


    # def test_06_nandez_1184014(self):
    #      from Chapter02.IrfanHernandezEnam1184014 import main
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

#    def test_07_HernandezTujuh1184014(self):
#        from Chapter02.IrfanHernandezTujuh1184014 import IrfanPut
#        thread1 = IrfanPut("Thread Put", 1, "miramas")
#        thread1.start()
#        thread1.join()
#        respon=self.readfile('./Chapter02/miramas.txt')
#        self.assertNotRegex(respon, "Kosong")
#    
#    
#    def test_07_alifTujuh1184068(self):
#        from Chapter02.AlifTujuh1184068 import alifTujuh1184068,alifHandlingFile  
#        threadutama = alifTujuh1184068("Thread Utama ", 2,5,5,'alip')
#        threadhandling= alifHandlingFile("Thread handling File ", 1,'alip')
#        threadhandling.start()
#        threadutama.start()
#        threadhandling.join()
#        threadutama.join()
#        respon=self.readfile('./Chapter02/alip.txt')
#        self.assertNotRegex(respon, "kosong")
    
    # def test_07_hanifTujuh1184058(self):
    #      from Chapter02.HanifTujuh1184058 import HanifTujuh1184058, HanifCopy
    #      thread1 = HanifCopy("Thread Copy File ",1 , 'pokemon.txt')
    #      thread2 = HanifTujuh1184058("Thread Utama ", 2, 5, 'pokemon.txt')
    #      thread2.start()
    #      thread1.start()
    #      thread2.join()
    #      thread1.join()
    #      respon=self.readfile('./Chapter02/pokemon.txt')
    #      self.assertNotRegex(respon, "Kosong")

    # def test_06_bahar_1184002(self):
    #     from Chapter02.baharenam1184002 import main
    #     response =  main()
    #     self.assertEqual(response, True)
        
    #def test_06_josuansef_1184091(self):
    #     from Chapter02.JosuansefEnam_1184091 import main
    #     response =  main()
    #     self.assertEqual(response, True)


#    def test_07_raviTujuh1184040(self):
#        from Chapter02.raviTujuh1184040 import raviTujuh1184040,raviMenulis 
#        threadutama = raviTujuh1184040("Thread Utama ", 2,5,5,'ravi')
#        threadravi2= raviMenulis("Thread raviMenulis File ", 1,'ravi')
#        threadravi2.start()
#        threadutama.start()
#        threadravi2.join()
#        threadutama.join()
#        respon=self.readfile('./Chapter02/ravi.txt')
#        self.assertNotRegex(respon, "kosong")
    
    # def test_07_OkkyTujuh1184087(self):
    #     from Chapter02.OkkyTujuh1184087 import Person,okky 
    #     t1 = Person("Thread Utama ", 1,'okky.txt')
    #     t2 = okky("Thread kedua File ", 2,5,'okky.txt')
    #     t2.start()
    #     t1.start()
    #     t2.join()
    #     t1.join()
    #     respon=self.readfile('./Chapter02/okky.txt')
    #     self.assertNotRegex(respon, "kosong")

    # def test_07_raviTujuh1184040(self):
    #     from Chapter02.raviTujuh1184040 import raviTujuh1184040,raviMenulis 
    #     threadutama = raviTujuh1184040("Thread Utama ", 2,5,5,'ravi')
    #     threadravi2= raviMenulis("Thread raviMenulis File ", 1,'ravi')
    #     threadravi2.start()
    #     threadutama.start()
    #     threadravi2.join()
    #     threadutama.join()
    #     respon=self.readfile('./Chapter02/ravi.txt')
    #     self.assertNotRegex(respon, "kosong")
    
#     def test_07_AnisaTujuh1184016(self):
#         from Chapter02.AnisaRosalinaTujuh1184016 import Anisa
#         thread1 = Anisa("Thread Put", 1, "Cocktile")
#         thread1.start()
#         thread1.join()
#         respon=self.readfile('./Chapter02/Cocktile.txt')
#         self.assertNotRegex(respon, "Kosong")

    # def test_07_AnisaTujuh1184016(self):
    #     from Chapter02.AnisaRosalinaTujuh1184016 import Anisa
    #     thread1 = Anisa("Thread Put", 1, "Cocktile")
    #     thread1.start()
    #     thread1.join()
    #     respon=self.readfile('./Chapter02/Cocktile.txt')
    #     self.assertNotRegex(respon, "Kosong")
    


    # def test_07_AriyoTujuh1184056(self):
    #     from Chapter02.AriyoTujuh1184056 import ayomaju
    #     thread1 = ayomaju("Thread Put", "AriyoTujuh")
    #     thread1.start()
    #     thread1.join()
    #     respon=self.readfile('./Chapter02/AriyoTujuh')
    #     self.assertNotRegex(respon, "Kosong")

    # def test_07_bahartujuh1184002(self):
    #     from Chapter02.bahartujuh1184002 import BaharQue,Bahartujuh1184002
    #     ti= BaharQue("Thread 1 ",'kodepos')
    #     tl = Bahartujuh1184002("Thread 2",'kodepos')
    #     ti.start()
    #     tl.start()
    #     ti.join()
    #     tl.join()
    #     respon=self.readfile('./Chapter02/kodepos')
    #     self.assertNotRegex(respon, "Gak Boleh Kosong")

    # def test_07_parhanTujuh1184042(self):
    #     from Chapter02.ParhanTujuh1184042 import parhanTujuh1184042,parhanmanajemenFile 
    #     threadutama = parhanTujuh1184042("Thread Utama ", 2,5,5,'apigempa')
    #     threadmanajemen= parhanmanajemenFile("Thread manajemen File ", 1,'apigempa')
    #     threadmanajemen.start()
    #     threadutama.start()
    #     threadmanajemen.join()
    #     threadutama.join()
    #     respon=self.readfile('./Chapter02/apigempa.txt')
    #     self.assertNotRegex(respon, "kosong")

    # def test_07_idaTujuh1184113(self):
    #     from Chapter02.IdaTujuh1184113 import idaTujuh1184113,Director
    #     threadutama = idaTujuh1184113("Thread Utama ", 2,5,5,'ida')
    #     threaddirector= Director("Thread Director ", 1,'ida')
    #     threaddirector.start()
    #     threadutama.start()
    #     threaddirector.join()
    #     threadutama.join()
    #     respon=self.readfile('./Chapter02/ida.txt')
    #     self.assertNotRegex(respon, "kosong")
    
    #def test_07_idaTujuh1184113(self):
    #    from Chapter02.IdaTujuh1184113 import idaTujuh1184113,Director
    #    threadutama = idaTujuh1184113("Thread Utama ", 2,5,5,'ida')
    #    threaddirector= Director("Thread Director ", 1,'ida')
    #    threaddirector.start()
    #    threadutama.start()
    #    threaddirector.join()
    #    threadutama.join()
    #    respon=self.readfile('./Chapter02/ida.txt')
    #    self.assertNotRegex(respon, "kosong")
    
    def test_07_rizaluarditujuh_1184102(self):
        from Chapter02.RizaluardiTujuh1184102 import RizaluardiIms,RizaluardiTujuh1184102
        nganu1 = RizaluardiIms("Thread 1", 'provinsi')
        nganu2 = RizaluardiTujuh1184102("Thread 2",'provinsi')
        nganu1.start()
        nganu2.start()
        nganu1.join()
        nganu2.join()
        respon=self.readfile('./Chapter02/provinsi')
        self.assertNotRegex(respon, "Jangan kosong datanya")
        
    #def test_07_josuanseftujuh1184091(self):
    #   from Chapter02.JosuansefTujuh_1184091 import Josuansef1184091Tujuh_Producer,Josuansef1184091Tujuh_Consumer
    #   threadjosuaproducer = Josuansef1184091Tujuh_Producer("Thread utama ", 2,5,5,'joss')
    #   threadjosuaconsumer = Josuansef1184091Tujuh_Consumer("Thread baca file ", 1,'joss')
    #   threadjosuaconsumer.start()
    #   threadjosuaproducer.start()
    #   threadjosuaconsumer.join()
    #   threadjosuaproducer.join()
    #   respon=self.readfile('./Chapter02/joss')
    #   self.assertNotRegex(respon, "kosong")

    # def test_07_josuanseftujuh1184091(self):
    #     from Chapter02.JosuansefTujuh_1184091 import Josuansef1184091Tujuh_Producer,Josuansef1184091Tujuh_Consumer
    #     threadjosuaproducer = Josuansef1184091Tujuh_Producer("Thread utama ", 2,5,5,'joss')
    #     threadjosuaconsumer = Josuansef1184091Tujuh_Consumer("Thread baca file ", 1,'joss')
    #     threadjosuaconsumer.start()
    #     threadjosuaproducer.start()
    #     threadjosuaconsumer.join()
    #     threadjosuaproducer.join()
    #     respon=self.readfile('./Chapter02/joss')
    #     self.assertNotRegex(respon, "kosong")


    #def test_07_iraTujuh1184024(self):
    #    from Chapter02.IraTujuh1184024 import iraTujuh1184024,iraHandlingFile  
    #    threadutama = iraTujuh1184024("Thread Utama ", 2,5,5,'ira')
    #    threadhandling= iraHandlingFile("Thread handling File ", 1,'ira')
    #    threadhandling.start()
    #    threadutama.start()
    #    threadhandling.join()
    #    threadutama.join()
    #    respon=self.readfile('./Chapter02/ira.txt')
<<<<<<< HEAD
    #    self.assertNotRegex(respon, "kosong")

    def test_07_vickyTujuh1184037(self):
        from Chapter02.VickyTujuh1184037 import vickysaf
        thread1 = vickysaf("Thread Put", "vicky")
        thread1.start()
        thread1.join()
        respon=self.readfile('./Chapter02/vicky')
        self.assertNotRegex(respon, "Kosong")
=======
    #    self.assertNotRegex(respon, "kosong")
>>>>>>> 5fe2184dfac85a8ef8e1a2b9f730486108983e6c
