from Hafta13_Sec2.Universite import akademisyen, ogrenci

akademisyen1 = akademisyen('Betul', 'Arac', 123456, 'P', 12)
akademisyen1.adi = "Begum"
akademisyen1.setGelirCarpani(3)

print("Maası = "+akademisyen1.adi)
akademisyen1.bilgileri_yaz()
akademisyen1.akademik_bilgileri_ekle()
akademisyen1.bilgileri_oku()

print("gelir Carpanı = " + str(akademisyen1.getGelirCarpani()))

akademisyen2 = akademisyen('Arya', 'Aydın', 9876, 'D', 10)
print(akademisyen2.getGelirCarpani())
akademisyen2.bilgileri_yaz()
akademisyen2.akademik_bilgileri_ekle()
print("Akademisyen 2 nin bilgileri getiriliyor...")
akademisyen2.bilgileri_oku()

ogr1 = ogrenci('Omer', 'Gurbuz', 123, 'Ece')
print("Ogrencinin bağlı olduğu danışman bilgileri getiriliyor")
ogr1.akademisyenbilgilerigetir()

akademisyen1.kimim()
ogr1.kimim()




