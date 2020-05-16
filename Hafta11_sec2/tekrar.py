from functools import reduce

ogrenciler = [[1,("A", 45), ("O",67), ("F", 92)], [ 2,("A",33), ("O",90)],
              [3,("A", 54), ("F", 56)],
              [4,("A",67), ("O",50), ("O",20), ("F", 92)]]
dict_isim = {1: "Omer", 2: "Betul", 3: "Gizem", 4:"Gamze"}


sonuc = list(map(lambda x: [x[0]] + list(map( lambda y: (y[1]*0.3) if (y[0] == "A") else (y[1] * 0.4 if (y[0] == "F") else y[1] * 0.05), x[1:] )), ogrenciler))
print(sonuc)
sonuc = list(map(lambda x: [dict_isim[x[0]]] + ["Kaldı" if x[1] < 60 else "Geçti"], list(map(lambda x: [x[0]] + [reduce(lambda a,b: a+b , x[1:] )], sonuc))))
print(sonuc)

def dikdörgenmi(dizi):
    flag = 0
    for i in range(len(dizi)):
        for j in range(i+1, len(dizi)):
            if i!=j and dizi[i] == dizi[j]:
                flag = flag +1
    if flag ==2:
        return True
    else:
        return False



dizi = [[23,34,56,67], [12,12,12,12], [45,67,88,3], [12,12,34,34], [11,56,11,56]]

sonuc = list(map(lambda x: "Kare" if (x[0] == x[1] == x[2] == x[3]) else("Dikdörtgen " if (dikdörgenmi(x)) else  "ne Kare ne dikdörtgen"), dizi))
print(sonuc)



