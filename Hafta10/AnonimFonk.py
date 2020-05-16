#bubble sort
dizi = [4,6,77,5,34,23,12,67,54]
for i in range (0, len(dizi)):
    for j in range(0,len(dizi)-i-1):
        if dizi[j] > dizi[j+1]:
            #gecici = dizi[j+1]
            #dizi[j+1] = dizi[j]
            #dizi[j] = gecici
            [dizi[j], dizi[j+1]] = [dizi[j+1], dizi[j]]
print(dizi)


#selection sort
dizi = [4,6,77,5,34,23,12,67,54]
for i in range(0,len(dizi)):
    poz = i
    for j in range(i+1,len(dizi)):
        if(dizi[j] < dizi[poz]):
            poz = j
    gecici = dizi[i]
    dizi[i] = dizi[poz]
    dizi[poz] = gecici


#insertion sort
dizi = [4,6,77,5,34,23,12,67,54]

for i in range(1,len(dizi)):
    key = dizi[i]
    j = i-1
    while(key < dizi[j] and j >= 0):
        dizi[j+1] = dizi[j]
        j = j-1
    dizi[j+1] = key
print(dizi)
def merge(A, baslangic, orta, bitis):
    L = A[baslangic:orta+1]
    U = A[orta+1:bitis+1]
    i=j=0
    for k in range(baslangic, bitis):
        if L[i] <= U[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = U[j]
            j=j+1

def merge_sort(A, baslangic, bitis): # 0 - 9
    if baslangic < bitis:
        orta = (baslangic + bitis) // 2
        merge_sort(A, baslangic, orta)
        merge_sort(A, orta + 1, bitis)
        merge(A, baslangic, orta, bitis)


#merge sort
dizi = [4,6,77,5,34,23,12,67,54]
merge_sort(dizi, 0, len(dizi)-1)



















