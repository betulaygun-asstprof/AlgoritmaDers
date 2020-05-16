class ogrenci:
    ad= "betul"
    soyad="aygun"

    def yazdir(self):
        print(self.ad)
        print(self.soyad)
    def ortalama(self, vize, final):
        return vize*0.40 + final*0.60

nesne = ogrenci()
print(nesne.ad, "-", nesne.soyad)
nesne.yazdir()

print("ortalama = ", nesne.ortalama(60,80))

class cokgen:
    def __init__(self, g, h):
        self.genislik = g
        self.yukseklik = h

    def alan(self):
        return self.yukseklik * self.genislik
dikdortgen = cokgen(5,2)
print(dikdortgen.yukseklik)
print(dikdortgen.alan())

class urun:
    def __init__(self):
        self.__fiyat = 56 #fiyat değişkeninin kapsüllemiş oluyorsunuz. Buna yeni bir değer atamazsınız.
        self.miktar = 12
    def yazdirFiyat(self):
        print(self.__fiyat)
    def yazdirMiktar(self):
        print(self.miktar)
    def setFiyat(self, fiyat):
        self.__fiyat = fiyat

u = urun()
u.setFiyat(20)
u.miktar = 18

u.yazdirFiyat()
u.yazdirMiktar()

class kus:  #superclass - süpersınıf
    tur_ad=""
    kus_ad=""

    def isimYaz(self):
        print("Tur adi = ",self.tur_ad)
        print("Kus ismi = ", self.kus_ad)

class evcil_kus(kus): #subclass - alt sını
    kanat_uzunlugu = "0"
    agirlik = "0"

class muhabbet_kus(evcil_kus):
    ses_yukselik = 30

pegy = muhabbet_kus()
pegy.tur_ad = "Muhabbet"
pegy.kus_ad = "Pigy"
pegy.kanat_uzunlugu = "150"

pegy.isimYaz()

class kedi:
    def ses(self):
        print("miyav")
class kopek:
    def ses(self):
        print("hav hav")
class kus:
    def ses(self):
        print("cik cik")

def hayvansSes(hayvan):
    hayvan.ses()

ke = kedi()
ko = kopek()
ku = kus()

hayvansSes(ke)

dizi =[12,34,44,15,67,89, 12,34, 12, 10]
#insertion sort
for i in range(1, len(dizi)):
    j = i-1
    key = dizi[i]
    while(j>=0 and key < dizi[j]):
        dizi[j+1] = dizi[j]
        j = j-1
    dizi[j+1] = key
print(dizi)


