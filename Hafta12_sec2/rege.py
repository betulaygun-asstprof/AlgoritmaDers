class universite_kisiler:
    def __init__(self,ad,soyad,tckimlikno):
        self.adi=ad
        self.soyadi=soyad
        self.tckimlikno=tckimlikno

    def ekle(self):
        try:
            dosyam = open("kisiler"+self.adi+".txt", mode='w', encoding='utf-8')
            dosyam.write("Eklenen Kişi \n")
            dosyam.write(self.adi + "\n")
            dosyam.write(self.soyadi + "\n")
            dosyam.write(str(self.tckimlikno) + "\n")
        except:
            print("HataAlındı")
        finally:
            dosyam.close()


    def ozetle(self):
        try:
            dosyam = open("kisiler"+self.adi+".txt", mode='r', encoding='utf-8')
            print(dosyam.read())
        except:
            print("Hata Alındı")
        finally:
            dosyam.close()
    def kimim(self):
        print("ben kimim")


class akademik(universite_kisiler):
    maas=0
    def __init__(self, adi,soyadi,tckimlikno, saat, calisma_alani, unvan):
        universite_kisiler.__init__(self, adi,soyadi,tckimlikno)
        self.saat = saat
        self.calisma_alani = calisma_alani
        self.unvan = unvan
        self.__birimucret = 2
    def setBirimucret(self, ucret):
        self.__birimucret = ucret
    def getBirimucret(self):
        return self.__birimucret


    def maas(self):
        if self.unvan == 'P':
            maas = self.saat * 300 * self.__birimucret
        else:
            maas = self.saat * 200 * self.__birimucret
        return maas

    def akademik_bilgi_ekle(self):
        try:
            dosyam = open("kisiler"+self.adi+".txt", mode='a', encoding='utf-8')
            maas = self.maas()
            dosyam.write(str(self.maas())+ "\n")
            dosyam.write(self.unvan + "\n")
        except:
            print("HataAlındı")
        finally:
            dosyam.close()
class ogrenci(universite_kisiler):
    def __init__(self,adi,soyadi,tckimlikno, calisma_alani, hocaadi):
        universite_kisiler.__init__(self, adi, soyadi, tckimlikno)
        self.calisma_alani = calisma_alani
        self.hocaadi = hocaadi

    def hoca_ozetle(self):
        try:
            dosyam = open("kisiler" + self.hocaadi + ".txt", mode='r', encoding='utf-8')
            print(dosyam.read())
        except:
            print("Hata Alındı...")
        finally:
            dosyam.close()
    def kimim(self):
        print("Ben öğrenciyim.")


from Hafta12_sec2.rege import akademik, ogrenci, universite_kisiler


calisan = akademik('Betül', 'Aygün', 1234567, 30, 'Algoritmalar', 'P')
calisan.ekle()
calisan.ozetle()
print(calisan.maas())
calisan.akademik_bilgi_ekle()
calisan.ozetle()
calisan2 = akademik('Ece', 'Aygün', 345, 20, 'Matematik', 'D')
calisan2.ekle()
calisan2.akademik_bilgi_ekle()
calisan2.ozetle()
calisan2.setBirimucret(3)
print(calisan.getBirimucret())
print(calisan2.getBirimucret())


ogr1 = ogrenci('Arya', 'Ardınc', 123, 'Güvenlik', 'Betül')
print("Ogrencinin Hoca Bilgileri Getiriliyor..")
ogr1.hoca_ozetle()
ogr1.hocaadi = 'Ece'
ogr1.hoca_ozetle()
ogr1.kimim()







