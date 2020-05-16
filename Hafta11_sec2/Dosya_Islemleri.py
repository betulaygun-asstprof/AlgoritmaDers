try:
    benim_dosyam = open(file=r"C:\Users\Akademik\Desktop\data.csv", mode = "a", encoding="utf-8")
    benim_dosyam.write("3,9")
    benim_dosyam.write("Benim Adım Ece \n")
    liste = ["portakal \t", "elma \t", "muz \t"]
    benim_dosyam.writelines(liste)
except FileNotFoundError:
    print("Dosya bulunamadı..")
finally:
    benim_dosyam.close()

with open(file=r"C:\Users\Akademik\Desktop\data.csv", mode = "r", encoding="utf-8") as benim_dosyam:
    #print(benim_dosyam.readlines())
    for satir in benim_dosyam.readlines():
        if "Ece" in satir:
            print("*************" + satir)
        else:
            print(satir)





