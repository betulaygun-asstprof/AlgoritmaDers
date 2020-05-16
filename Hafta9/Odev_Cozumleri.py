#Bilgisayar 1-100 arasında bir sayı tutacak
import random
sayi = random.randint(1,100)
print(sayi)
sayac = 0
while(True):
    if sayac < 10:
        try:
            tahmin = int(input("Bir sayı tahmin ediniz: "))
            sayac = sayac + 1
            if tahmin < sayi:
                print("Daha büyük bir sayı giriniz.")
            elif tahmin > sayi:
                print("Daha küçük bir sayı giriniz.")
            else:
                print(str(sayac) + ". tahminde doğru bildiniz.")
                break
        except:
            print("Hatalı işlem gerçekleşti.")
    else:
        print("10 tahmin hakkını kullandınız.")
        break
