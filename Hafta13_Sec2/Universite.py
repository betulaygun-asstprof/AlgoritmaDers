class kisiler:
    def __init__(self, adi="Betul", soyadi="Aygun", tckimlikno=1234):
        self.adi = adi
        self.soyadi = soyadi
        self.tckimlikno= tckimlikno

    def bilgileri_yaz(self):
        try:
            dosyam = open(file="Kisi" + self.adi + "Dosyasi", mode='w', encoding='utf-8')
            dosyam.write("Adı = " + self.adi + "\n")
            dosyam.write("Soyadı = " + self.soyadi +"\n")
            dosyam.write("Tc Kimlik No = " + str(self.tckimlikno) + "\n")
        except:
            print("Hata alındı...")
        finally:
            dosyam.close()

    def bilgileri_oku(self):
        try:
            dosyam = open(file="Kisi" + self.adi + "Dosyasi", mode='r', encoding='utf-8')
            print(dosyam.read())
        except:
            print("Hata alındı...")
        finally:
            dosyam.close()

    def kimim(self):
        print("Ben bir kişiyim.")

class akademisyen(kisiler):

    def __init__(self, adi, soyadi, tckimlikno, unvan, saat):
        kisiler.__init__(self, adi, soyadi, tckimlikno)
        self.unvan = unvan
        self.saat = saat
        self.__gelircarpani = 2

    def setGelirCarpani(self, carpan):
        self.__gelircarpani = carpan
    def getGelirCarpani(self):
        return self.__gelircarpani

    def maas_Hesapla(self):
        if(self.unvan == 'P'):
            return self.saat * 300 * self.__gelircarpani
        else:
            return self.saat * 200 * self.__gelircarpani

    def akademik_bilgileri_ekle(self):
        try:
            dosyam = open(file="Kisi" + self.adi + "Dosyasi", mode='a', encoding='utf-8')
            dosyam.write("Unvan = " + self.unvan + "\n")
            dosyam.write("Maas = " + str(self.maas_Hesapla()) +"\n")
        except:
            print("Hata alındı...")
        finally:
            dosyam.close()

    def kimim(self):
        print("Ben bir akademisyenim.")


class ogrenci(kisiler):
    def __init__(self, adi, soyadi, tckimlikno, akademisyenadi):
        kisiler.__init__(self, adi, soyadi, tckimlikno)
        self.akademisyenadi = akademisyenadi

    def akademisyenbilgilerigetir(self):
        try:
            dosyam = open(file="Kisi" + self.akademisyenadi + "Dosyasi", mode='r', encoding='utf-8')
            print(dosyam.read())
        except:
            print("Hata alındı...")
        finally:
            dosyam.close()
    def kimim(self):
        print("Ben bir öğrenciyim.")








# kisi1 = kisiler("Ece", "Aydın", 111)
# kisi1.bilgileri_yaz()
# kisi1.bilgileri_oku()

