# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 00:09:02 2021

@author: MERVE ALKAN
"""



#yaziyi girdigimiz kisim
def yazial():
    yazi = input("Yazinizi giriniz : ")
    return yazi

#kac sayi atlatarak sifrelemek istedigimiz kisim
def sayial():
    sayi = int(input("Kac sayi atlatmak istiyorsunuz : "))
    if sayi >= 1 and sayi <= 26:
         return sayi

    else:
         print("Lutfen 0 ile 26 arasi bir deger giriniz")
         return sayial()
        
#sifreleme kismi
def sifreleme(yazi):
    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']
    buyukAlfabe = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W' , 'X', 'Y', 'Z']
    sifre = ""
    
    for i in yazi:
        if i.isupper():
            sifre += buyukAlfabe[(buyukAlfabe.index(i) + sayi) % len(alfabe)]

        else:
            sifre = sifre + alfabe[(alfabe.index(i)+sayi) % len(alfabe)]
    print("Yazinin sifrelenmis hali : " + sifre)

#eski haline cevirme kismi (sifre cozucu)
    teyit = input("Sonucun dogrulugunu teyit etmek ister misiniz? [e - h]\n")
    if teyit == "e" or teyit == "E":
         cozucu = ""
         for a in sifre:
            cozucu = cozucu + alfabe[(alfabe.index(a)-sayi) % len(alfabe)]
         print("Yazinin sifresi cozulmus hali : " + cozucu)

    elif teyit == "h" or teyit == "H":
        print("Kullandiginiz icin tesekkurler. Hoscakalin.")

    else:
        return sifreleme(yazi)

yazi = yazial()
sayi = sayial()
sifreleme(yazi)