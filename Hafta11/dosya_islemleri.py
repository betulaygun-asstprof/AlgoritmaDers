try:
    benim_dosyam = open(file="deneme.csv", mode="w", encoding="utf-8")
    benim_dosyam.write("Merhaba \n")
    benim_dosyam.write("Benim adım Ece \n")
    liste = ["portakal \n", "elma \n"]
    benim_dosyam.writelines(liste)

except FileNotFoundError:
    print("Dosya Bulunamadı...")
finally:
    benim_dosyam.close()

with open(file="deneme.csv", mode="r", encoding="utf-8") as benim_dosyam:

    for satir in benim_dosyam.readlines():
        if "Ece" in satir:
            print("********" + satir)
        else:
            print(satir)









