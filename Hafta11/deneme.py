class kisiler:
    def __init__(self, a, s, t):
        self.adi = a
        self.soyadi = s
        self.tckimlikno = t
    def bilgiOzeti(self):
        print("Kisinin Adi: ", self.adi)
        print("Kisinin Soyadi: ", self.soyadi)
        print("Kisinin TcKimlikNo: ", self.tckimlikno)

class personel(kisiler):
    def __init__(self, a,s,t,g):
        super().__init__(a, s, t)
        self.gunsayisi = g
        self.__sabitmaas = 1200
    def maasHesaplama(self):
        self.maas = self.gunsayisi * 200 + self.__sabitmaas
        return self.maas

    def setSabitmaas(self, maas):
        self.__sabitmaas = maas


class akademik(personel):

    def __init__(self, a,s,t,g, unvan):
        super().__init__(a,s,t,g)
        self.unvan = unvan
    def ekGelir(self):
        if self.unvan == "P":
            self.ekgelir = self.gunsayisi * 100
        else:
            self.ekgelir = self.gunsayisi * 50
        return self.ekgelir

class idari(personel):

    def __init__(self, a,s,t,g, seviye):
        super().__init__(a,s,t,g)
        self.seviye = seviye
    def ekGelir(self):
        if self.seviye == 1:
            self.ekgelir = self.gunsayisi * 3
        elif self.seviye == 2:
            self.ekgelir = self.gunsayisi * 2
        else:
            self.ekgelir = self.gunsayisi * 1
        return self.ekgelir


class ogrenci(kisiler):
    def __init__(self, kisi, d, t):
        super().__init__(kisi.adi, kisi.soyadi, kisi.tckimlikno)
        self.ders = d
        self.tezkonusu = t
    def ogrenciOzeti(self):
        print("Ogrencinin dersi: ", self.ders)
        print("Ogrencinin tez konusu: ", self.ders)



k = kisiler("betul", "aygun", 1234)
n = ogrenci(k, "ders", "tez_konusu")
print(n.tckimlikno)

k = kisiler("ece", "yıldız", 123456)
k.bilgiOzeti()

per = personel(k.adi, k.soyadi, k.tckimlikno, 20)
print(type(per))
print(per.maasHesaplama())
per.setSabitmaas(1000)
per.bilgiOzeti()
aka = akademik(k.adi, k.soyadi, k.tckimlikno, per.gunsayisi, "P")
print(aka.adi)
print(aka.maasHesaplama())
print(aka.ekGelir())



