dizi = [[12,12,13,13],[2,2,2,2],[12,13,14,15], [12,3,12,3]]
sonuc = list(map(lambda x: "kare" if (x[0] == x[1] ==x[2] == x[3]) else "Kare değildir" ,dizi))
print(sonuc)

sonuc = list(map(lambda x: "kare" if (x[0] == x[1] ==x[2] == x[3])
else ("Dörtgendir" if((x[0] ==x[1] and x[2] ==x[3]) or (x[0] ==x[2] and x[1] ==x[3])
                      or (x[0] ==x[3] and x[1] ==x[2])) else "Başka şekildir")  ,dizi))
print(sonuc)

#Parça sayısı (0,10) arası için parça başına 5000,
#Parça sayısı [10,30) arası için parça başına 8000,
#Parça sayısı 30 ve yukarısı için parça başına 12000
dizi = [[2000, 45], [3000, 23], [1000, 7]]

maas = list(map(lambda x: (x[0] + x[1] * 5000) if x[1] <10 else
((x[0] + x[1] * 8000) if x[1] <10 else (x[0] + x[1] * 12000)) , dizi))
print(maas)


bolunen = 15
bolen = 3
sayac = 0
while (bolen <= bolunen):
    bolunen = bolunen - bolen
    sayac = sayac +1
print(sayac)


def recur_bolme(bolunen, bolen):
    if(bolunen < bolen):
        return 0
    return 1 + recur_bolme(bolunen-bolen, bolen)
print(recur_bolme(15,4))
