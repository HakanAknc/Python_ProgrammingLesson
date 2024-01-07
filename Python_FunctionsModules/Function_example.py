# Örnek1
"""
def yasHesapla(dogumYili):
    return 2023 - dogumYili

hakan = yasHesapla(2001)
evren = yasHesapla(2019)
caner = yasHesapla(2004)
eyupcan = yasHesapla(2011)

print(hakan,evren,caner,eyupcan)

# print(yasHesapla(2001),yasHesapla(2019))

def EmekliligKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f"Eemkliliğinize {emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz.")

EmekliligKacYilKaldi(2001,"Hakan")
"""

# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren python fonksiyonunu yazınız.
"""
def yazdir(kelime, adet):
    print(kelime * adet)

yazdir("Merhaba\n", 10)
"""

# 2- Gönderilen 2 sayı arasındaki tüm asal sayıları bulan python fonksiyon uygulamasını yapınız.

sayi1 = int(input("Sayi1: "))
sayi2 = int(input("Sayi2: "))

def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi1 > 1:
            for i in range(2, sayi):
                if(sayi % i == 0):
                    break
            else:
                print(sayi)

asalSayilariBul(sayi1,sayi2)