dizi = [[12,12,34,34],[1,2,3,4],[2,2,2,2],[12,10,10,12]]

def dörtgenmi(x):
    if ((x[0] ==x[1] and x[2] == x[3]) or (x[0] ==x[2] and x[1] == x[3])
                        or (x[0] ==x[3] and x[1] == x[1])):
        return True
    else:
        return False


sonuc = list(map(lambda x: "Karedir" if (x[0] == x[1] == x[2] == x[3])
else ("Dörtgendir " if (dörtgenmi(x)) else "Ne dörtgen ne Karedir"),dizi))
print(sonuc)


dizi = [[4000, 23],[2300, 32],[5000, 7]]
#	Parça sayısı (0,10) arası için parça başına 5000,
#	Parça sayısı [10,30) arası için parça başına 8000,
#	Parça sayısı 30 ve yukarısı için parça başına 12000

sonuc = list(map( lambda x: (x[0] + x[1] * 5000)  if(x[1] < 10)
else ( (x[0] + x[1] * 8000) if (x[1] < 30) else  (x[0] + x[1] * 12000)) , dizi))
print(sonuc)

#bolunen 15  bolen 4
 #15 -4 11 1
 #11-4 7 2
 #7-4 3 3

bolunen = 15
bolen = 3
sayac = 0
while(bolen <= bolunen):
    bolunen = bolunen - bolen
    sayac = sayac + 1

print(sayac)

def recur_bolme(bolunen,bolen):
    if(bolunen < bolen):
        return 0
    return 1 + recur_bolme(bolunen-bolen, bolen)
print(recur_bolme(14,3))






