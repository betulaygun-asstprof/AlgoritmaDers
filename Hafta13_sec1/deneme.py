from Hafta13_sec1.universite import akademisyen, ogrenci

hoca1 = akademisyen('Ece', 'Yılmaz', 12, 'P', 20)
hoca1.ekle()
hoca1.setGelirCarpani(3)
print("Gelir carpani = " + str(hoca1.getGelirCarpani()))
print("Maas = " + str(hoca1.maas()))
hoca1.akademisyen_bilgileri_ekle()
hoca1.bilgileri_getir()

hoca2 = akademisyen('Arya', 'Acar', 1234, 'D', 10)
hoca2.soyadi = "Arac"
hoca2.ekle()
hoca2.akademisyen_bilgileri_ekle()
print("Hoca 2 nin bilgileri getiriliyorr....")
hoca2.bilgileri_getir()

ogr1 = ogrenci('Ahmet', 'Can', 111, 'Ece')
print("Ogrencinin hocasının bilgileri getiriliyor...")
ogr1.Hoca_bilgileri_getir()

hoca2.kimim()
ogr1.kimim()