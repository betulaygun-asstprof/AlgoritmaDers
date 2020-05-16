class ogrenci:
    def __init__(self, adi, id, tipi):
        self.adi = adi
        self.id = id
        self.tip = tipi
    def urunFiyat(self):
         if self.tip =="A":
             self.Fiyat = 200
         else:
             self.Fiyat = 200
    def UrunOzetle(self):
        print("Urunun Adi = ", self.adi)
        print("Urunun ID = ", self.id)
        print("Urunun Tipi = ", self.tip)


