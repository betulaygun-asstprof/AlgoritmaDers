from functools import reduce


def kup(x):
    return x**3
g = lambda x: x**3
print(g(3))
tupe = (1,2,3,4,4)

isim = ["Betul", "Ece", "Ali", "Ayşe", "Fatma", "Arya", "Ahmet", "Mehmet"]
O = [23,67,43,11,23,45,67,89]
A = [67,22,89,76,56,43,23,45]
F = [98,22,13,45,87,65,45,43]
print(reduce(lambda x,y: x if x>y else y, O))
fac = 10
sonuc = reduce(lambda x,y: x+y, [x for x in range(1,fac)])
print(sonuc)
sonuc = map(lambda x,y,z: "Geçti" if (x*0.3 + y*0.3 + z*0.4) >= 60 else ("Butunlemeye kaldı" if (x*0.3 + y*0.3 + z*0.4) >= 40 else "Kaldı") , O, A, F)
liste = zip(isim, sonuc)


dizi = [23,45,None,45,67,77,None,45]
sonuc = reduce(lambda x,y:x+y, list(filter(lambda x: x != None, dizi))) / len(list(filter(lambda x: x != None, dizi)))
print(sonuc)
dizi=[12,-33,45,-32,12,-34,54]
sonuc = (reduce(lambda x,y: x+y, list(map(lambda x:0 if x<0 else 1, dizi))), reduce(lambda x,y: x+y, list(map(lambda x:0 if x>0 else 1, dizi))))
print(sonuc)






