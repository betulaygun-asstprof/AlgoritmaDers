class urun():

    def __init__(self, adi = "Kalem", id = 123):
        self.urunAdi = adi
        self.urunId = id
        self.__urunFiyat=300
    def seturunFiyat(self, fiyat):
        self.__urunFiyat = fiyat
    def geturunFiyat(self):
        return self.__urunFiyat

    def UrunBilgileriOzetle(self):
        print("Urunun Adı = ", self.urunAdi)
        print("Urunun Id = ", self.urunId)
        print("Urunun Fiyat = ", self.__urunFiyat)


nesne1 = urun("Silgi",1)
nesne1.seturunFiyat(150)
print(nesne1.geturunFiyat())
nesne1.UrunBilgileriOzetle()
# nesne2 = urun()
# nesne2.urunId = 1
# print(nesne2.urunAdi)
# nesne2.UrunBilgileriOzetle()

class calisan():
    def __init__(self, adi="Betul", soyadi="Aygün", kimlik=123):
        self.adi = adi
        self.soyadi = soyadi
        self.kimlik = kimlik
    def BilgiOzeti(self):
        print("Calisanın Adı = ", self.adi)
        print("Calisanın soyadı = ", self.soyadi)
        print("Calisanın kimlik = ", self.kimlik)


class akademik(calisan):
    def __init__(self, saat=2):
        calisan.__init__(self)
        self.derssaati = saat
    def maasHesaplama(self):
        return 200 * self.derssaati

# kisi = calisan("Ece", "Yılmaz", 1)
# kisi.BilgiOzeti()

personel = akademik()

personel.BilgiOzeti()
print(personel.maasHesaplama())


