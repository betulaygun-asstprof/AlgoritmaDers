dizi = [12,45,34,21,2,34,98,6,54]
#insertion sort

for i in range(1, len(dizi)):
    key = dizi[i]
    j = i-1
    while(j>=0 and key < dizi[j]):
        dizi[j+1] = dizi[j]
        j = j-1
    dizi[j+1] = key
print(dizi)

