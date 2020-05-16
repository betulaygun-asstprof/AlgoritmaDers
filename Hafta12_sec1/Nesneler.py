class urun:

    def __init__(self, adi="Kitap", id=123):
        self.urunadi = adi
        self.urunid = id
        self.__urunFiyat = 200

    def seturunFiyat(self, fiyat):
        self.__urunFiyat = fiyat

    def geturunFiyat(self):
        return self.__urunFiyat

    def bilgileriozetle(self):
        print("Urunun adı = ", self.urunadi)
        print("Urunun id = ", self.urunid)
        print("Urunun fiyat = ", self.__urunFiyat)

urun_nesnesi = urun()
urun_nesnesi.bilgileriozetle()
urun_nesnesi.urunadi = "Defter"
urun_nesnesi.urunid = 1
urun_nesnesi.seturunFiyat(500)
#urun_nesnesi.bilgileriozetle()
print(urun_nesnesi.geturunFiyat())

class calisan():
    def __init__(self, ad, soyadi, sicilNo, gun_sayisi):
        self.adi = ad
        self.soyadi= soyadi
        self.sicilNo = sicilNo
        self.gunsayisi = gun_sayisi
    def maasHesaplama(self):
        return 200 * self.gunsayisi

class akademik(calisan):
    def __init__(self):
        calisan.__init__(self)
        self.calismaalanları = "VeriTabanı"
        self.ders = "Matematik"

calisan1 = calisan("Betul", "Aygun", 123, 20)
calisan2 = calisan("Ece", "Yılmaz", 23, 12)







