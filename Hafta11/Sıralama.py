#buble sort (kabarcık sıralama)

# dizi = [34,56,10,88,76,12,34,54,21]
# dizi = ['e','f','a','c','b','g']
#
# for i in range(0, len(dizi)-1):
#     for j in range(0, len(dizi)-1-i):
#         if(dizi[j] > dizi[j+1]):
#             # gecici = dizi[j+1]
#             # dizi[j+1] = dizi[j]
#             # dizi[j] = gecici
#             [dizi[j], dizi[j+1]] = [dizi[j+1], dizi[j]]
#
# print(dizi)

# selection seçmeli sıralama
# dizi = [34,56,10,88,76,12,34,54,21]
# for i in range(0, len(dizi)):
#     en_kucuk_poz = i
#     for j in range(i+1, len(dizi)):
#         if(dizi[j] < dizi[en_kucuk_poz]):
#             en_kucuk_poz = j
#     #swap
#     gecici = dizi[i]
#     dizi[i] = dizi[en_kucuk_poz]
#     dizi[en_kucuk_poz] = gecici
#
# print(dizi)
dizi = [34,56,10,88,76,12,34,54,21]
#insetion eklemeli sıralama
for i in range(1,len(dizi)):
    key = dizi[i]
    j = i-1
    while(j >=0 and key < dizi[j]):
        dizi[j+1] = dizi[j]
        j = j-1
    dizi[j+1] = key

print(dizi)


