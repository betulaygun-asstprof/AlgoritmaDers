from functools import reduce

dikdörtgenler = [[2,3,1,2],[2,2,2,2],[3,4,5,2], [4,4,4,4]]

g = lambda x:True if (x[0]==x[1]==x[2]==x[3]) else False
sonuc = list(map(g, dikdörtgenler))
print(sonuc)
dizi_Ogrenci= ["Betul", "Ece", "Bengu", "Gurcan", "Mehmet", "Ahmet", "Ayse", "Esra"]
dizi_N1 = [56,32,12,45,67,89,34,56]
dizi_N2 = [67,34,23,12,33,45,56,43]
dizi_N3 = [45,99,76,34,56,76,12,54]

sonuc = list(zip(dizi_Ogrenci,list(map(lambda n1,n2: n1*0.3+n2*0.7,
                                  list(map(lambda x,y:x if (x>y) else y, dizi_N1, dizi_N2)), dizi_N3))))
print(sonuc)
#print(list(map(lambda x,y:(x>60), list(sonuc.values()), list(sonuc.keys()))))
print(list(filter(lambda x:x[1]>60, sonuc)))

liste = [23,45,55,66,23,12,34,56,43,45]
#çift ve teklerin sayısını bulalım
count_tek=0
count_cift=0
print(liste)
sonuc = [len(liste)-reduce(lambda x,y: x+y,list(map(lambda x: x%2, liste))),  reduce(lambda x,y: x+y,list(map(lambda x: x%2, liste)))]
print(list(map(lambda x: x%2, liste)))
print(sonuc)

#En küçük elemanı bulma
liste = [23,45,55,66,23,12,34,56,43,45]
sonuc = reduce(lambda x,y: x if(x<y) else y, liste)
print(sonuc)

siparisler = [[3455,"Python Öğreniyorum", 5,22],[2134,"Algoritma",4,33],[2311,"İstatiksel Analizler",1,54],[2388,"Matematik",5,12]]
sonuc = list(map(lambda x: (x[0], x[1] +10) if x[1] <100 else x, map(lambda x:(x[0], x[2]*x[3]), siparisler)))
print(sonuc)

siparisler = [[3455,("Python Öğreniyorum", 5,22), ("Python",2,24), ("Ptyh", 3,12)],[2134,("Algoritma",4,33), ("Karakedi",1,22)],[2311,("İstatiksel Analizler",1,54)],[2388,("Matematik",5,12), ("Geometri",1,20)]]

print(list(map(lambda x: x[1]*x[2], siparisler[0][1:])))

siparis_toplamlar = list(map(lambda x: [x[0]] + list(map(lambda y:y[1]*y[2], x[1:])), siparisler))
print(siparis_toplamlar)
siparis_2 = list(map(lambda x: [x[0]] + [reduce(lambda a,b:a+b , x[1:])] , siparis_toplamlar))
print(siparis_2)
sonuc = list(map(lambda x: x if x[1] > 100  else (x[0], x[1] + 10), siparis_2))
print(sonuc)