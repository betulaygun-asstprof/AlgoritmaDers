def topla(dizi):
    top = 0
    for i in range(len(dizi)):
        top += dizi[i]
    return top
def carp(dizi):
    carpma = 1
    for i in range(len(dizi)):
        carpma *= dizi[i]
    return carpma


# Arayuzden dizinin elemanları alıp, kulanıcıgı girdiği indekse göre dizideki elemanı döndürme
dizi = []
while(True):
     sayi = int(input("Bir sayı giriniz. (0 program çıkışı)"))
     if(sayi == 0):
         print("Çıkış yaptınız.")
         break
     dizi.append(sayi)
en_kucuk = dizi[0]
en_buyuk = dizi[0]

for i in range(1,len(dizi)):
    if en_kucuk > dizi[i]:
        en_kucuk = dizi[i]
    if en_buyuk < dizi[i]:
        en_buyuk = dizi[i]
print("en kücük sayı", en_kucuk)
print("en büyük sayı", en_buyuk)

aranan_sayi = int(input("aranacak sayıyı giriniz: "))
indeks = -1
for i in range(len(dizi)):
    if aranan_sayi == dizi[i]:
        indeks = i
        break

if(indeks == -1):
    print("bulunamadı")
else:
    print("indeks = ",i)

print(dizi.index(23))








