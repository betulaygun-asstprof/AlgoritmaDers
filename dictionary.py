# 2 rakamlı bir sayı girdiğimizde bunun yazı ile yazılsın.
dict_birler = {1: "bir", 2:"iki", 3:"üç", 4: "dört", 5: "bes", 6: "altı", 7: "yedi", 8: "sekiz", 9:"dokuz", 0:""}
dict_onlar = {1: "on", 2:"yirmi", 3:"otuz", 4: "kırk", 5: "elli", 6: "atmış", 7: "yetmiş", 8: "seksen", 9:"doksan", 0:""}

sayi = int(input("İki basamaklı bir sayı giriniz: "))

print(dict_onlar[sayi//10] , dict_birler[sayi%10])

