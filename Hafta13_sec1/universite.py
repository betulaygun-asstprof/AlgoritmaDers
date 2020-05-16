class kisiler:
    def __init__(self, adi, soyadi, tckimlikno):
        self.adi=adi
        self.soyadi=soyadi
        self.tckimlikno = tckimlikno
    def ekle(self):
        try:
            dosyam = open(file="Kisi"+self.adi+"dosyasi", mode='w', encoding='utf-8')
            dosyam.write("Adı = "+ self.adi + "\n")
            dosyam.write("Soyadı = " + self.soyadi + "\n")
            dosyam.write("Tc Kimlik No = " + str(self.tckimlikno) + "\n")
        except:
            print("Hata oldu...")
        finally:
            dosyam.close()
    def bilgileri_getir(self):
        try:
            dosyam = open(file="Kisi"+self.adi+"dosyasi", mode='r', encoding='utf-8')
            print(dosyam.read())
        except:
            print("Hata oldu...")
        finally:
            dosyam.close()
    def kimim(self):
        print("Ben bir kişiyim.")



class akademisyen(kisiler):

    def __init__(self, adi, soyadi, tckimlikno, unvan, saat):
        kisiler.__init__(self, adi, soyadi, tckimlikno)
        self.unvan = unvan
        self.saat = saat
        self.__gelirCarpani = 2
    def setGelirCarpani(self, carpan):
        self.__gelirCarpani = carpan
    def getGelirCarpani(self):
        return self.__gelirCarpani

    def maas(self):
        if self.unvan == 'P':
            return self.saat * 300 * self.__gelirCarpani
        else:
            return self.saat * 200 * self.__gelirCarpani

    def akademisyen_bilgileri_ekle(self):
        try:
            dosyam = open(file="Kisi"+self.adi+"dosyasi", mode='a', encoding='utf-8')
            dosyam.write("Unvan = "+ self.unvan + "\n")
            dosyam.write("Maas = " + str(self.maas()) + "\n")
        except:
            print("Hata oldu...")
        finally:
            dosyam.close()
    def kimim(self):
        print("Ben bir akademisyenim.")

class ogrenci(kisiler):
    def __init__(self, adi, soyadi, tckimlikno, hocaadi):
        kisiler.__init__(self, adi, soyadi, tckimlikno)
        self.hocaadi = hocaadi

    def Hoca_bilgileri_getir(self):
        try:
            dosyam = open(file="Kisi"+self.hocaadi+"dosyasi", mode='r', encoding='utf-8')
            print(dosyam.read())
        except:
            print("Hata oldu...")
        finally:
            dosyam.close()
    def kimim(self):
        print("Ben bir ogrenciyim.")


# kisi1 = kisiler("Betul", "Aygün", 1234)
# kisi1.ekle()







