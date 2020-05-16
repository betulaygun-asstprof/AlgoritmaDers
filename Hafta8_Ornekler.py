def recur_top(n):
    if n < 1:
        return 0
    return (n / (n+1)) + recur_top(n-1)

def dongu_top(n):
    toplam = 0
    for i in range(1, n+1):
        toplam = toplam + i / (i + 1)
    return toplam
def topla_dizi(dizi):
    toplam = 0
    for i in range(len(dizi)):
        toplam += dizi[i]
    return toplam
def carp_dizi(dizi):
    carpim = 1
    for i in range(len(dizi)):
        carpim *= dizi[i]
    return carpim
def en_kucuk_eleman(dizi):
    en_kucuk = dizi[0]
    for i in range(len(dizi)):
        if en_kucuk > dizi[i]:
            en_kucuk= dizi[i]
    return en_kucuk

def en_buyuk_eleman(dizi):
    en_buyuk = dizi[0]
    for i in range(len(dizi)):
        if en_buyuk < dizi[i]:
            en_buyuk= dizi[i]
    return en_buyuk

# dizi = []
# while(True):
#     sayi = int(input("n sayısı giriniz: "))
#     if sayi==0:
#         print("Donguden cıktınız")
#         break
#     dizi.append(sayi)
#
# print("elemanların en büyüğü = ", en_buyuk_eleman(dizi))
# print("elemanların en küçüğü = ", en_kucuk_eleman(dizi))
#
# print("metod ile elemanların en büyüğü = ", max(dizi))
# print("metod ile elemanların en küçüğü = ", min(dizi))
#
# sayi = int(input("Aramak istediğiniz sayıyı giriniz."))
# indeks = []
# for i in range(len(dizi)):
#     if sayi == dizi[i]:
#         indeks.append(i)
#
# if indeks == -1:
#     print("bulunamadı")
# else:
#     print("yazılan metod indeks", indeks)
#
# print("python indeks",dizi.index(sayi))

dict_birler = {1: "bir", 2:"iki", 3:"üç", 4: "dört", 5:"beş", 6:"altı", 7: "yedi", 8:"sekiz", 9:"dokuz", 0:""}
dict_onlar = {1: "on", 2:"yirmi", 3:"otuz", 4: "kırk", 5:"elli", 6:"atmış", 7: "yetmiş", 8:"seksen", 9:"doksan", 0:""}

sayi = int(input("İki basamaklı bir syaı giriniz: "))

print(dict_onlar[sayi // 10] , dict_birler[sayi%10])




