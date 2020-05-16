class Urun:
    def __init__(self, adi="kalem", id=23, fiyat=120):
        self.UrunAdi = adi
        self.UrunId = id
        self.__UrunFiyat = fiyat

    def setUrunFiyat(self,fiyat):
        self.__UrunFiyat = fiyat

    def getUrunFiyat(self):
        return self.__UrunFiyat

    def UrunBilgileriOzetle(self):
        print("Urun Adi = ", self.UrunAdi)
        print("Urun Id = ", self.UrunId)
        print("Urun Fiyat = ", self.__UrunFiyat)

class Meyve(Urun):
    def __init__(self, vitamin):
        Urun().__init__()
        self.Vitamin = vitamin
    def VitaminOzet(self):
        print("Vitamin = " , self.Vitamin)

class Sebze(Urun):
    def __init__(self, vitamin, adi, id, fiyat):
        Urun().__init__(adi, id, fiyat)
        self.Vitamin = vitamin
    def VitaminOzet(self):
        print("Vitamin = " , self.Vitamin)



obj = Urun("Silgi", 11, 100)
#obj.UrunAdi ="Defter"
#obj.setUrunFiyat(150)
obj.UrunBilgileriOzetle()

mey = Meyve("C")
mey.VitaminOzet()





