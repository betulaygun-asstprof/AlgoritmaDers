def recur_dizi(n):
    if n < 1:
        return 0
    return (n / (n+1)) + recur_dizi(n-1)

n = int(input("Lutfen n sayısı giriniz: "))
print(recur_dizi(n))
top = 0
for i in range(1,n+1):
    top = top + i / (i+1)

print("dongu = ", top)