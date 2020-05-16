#bubble sort
def swap(a,b):
    gecici = a
    a = b
    b = gecici
    return (b,a)
dizi = [12,34,23,14,78,56,34,56,78,99]
#dizi = ['b','e','t','ü','a','l']

# for i in range(0, len(dizi)-1):
#     for j in range(0, len(dizi)-i-1):
#         if (dizi[j] > dizi[j+1]):
#             (dizi[j], dizi[j+1]) = (dizi[j+1], dizi[j])
# print(dizi)


# for i in range(0, len(dizi)):
#     en_kucuk_poz = i
#     for j in range(i+1, len(dizi)):
#         if dizi[j] < dizi[en_kucuk_poz]:
#             en_kucuk_poz = j
#     gecici = dizi[i]
#     dizi[i] = dizi[en_kucuk_poz]
#     dizi[en_kucuk_poz] = gecici
# print(dizi)


import csv
with open(file="deneme.csv", mode="w", newline="") as benim_dosyam:
    yazıcı = csv.writer(benim_dosyam)
    yazıcı.writerow(["nnn"])
    yazıcı.writerow(["deneme"])

with open(file="deneme.csv", mode="r") as f:
    okuyucu = csv.reader(f)
    for line in okuyucu:
        print(line)





