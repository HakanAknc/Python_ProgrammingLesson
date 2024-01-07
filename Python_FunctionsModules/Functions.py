"""
* Fonksiyon tanımlamak
Fonksiyon tanımlamak için def kelimeisni kullanıyoruz:
def fonksiyon_adi():

- def yazdıktan sonra fonksiyona isim veriyoruz
- türkçe karekter kullanmıyoruz
- tanımladıktan sonra en sona parantez ve iki nokta üst üste ekliyoruz
"""

# İlk fonksiyon tanımlama
"""
def fonksiyon_adi():
    print("Merhaba Dünya")

fonksiyon_adi()
"""

# Örnek 1
"""
def selamlama():
    print("Merhaba dünya!")
    print("Nasılsın")
    print("Napıyorsun")

selamlama()
"""

# Örnek 2
"""
sayi = int(input("Lütfen bir sayı giriniz: "))

def tek():
    print("Girdiğiniz sayı bir tek sayıdır.")

def cift():
    print("Girdiğiniz sayı bir çift sayıdır.")

if sayi % 2 == 0:
    cift()
else:
    tek()
"""

# def toplama(a,b,c):
#     print("Toplamları: ",a+b+c)

# toplama(3,4,5)
# toplama(10,11,12)


# Faktöriyel hesaplama
def faktoriyel(sayı):
    faktoriyel = 1
    if(sayı == 0 or sayı == 1):
        print("Faktoriyel: ",faktoriyel)
    else:
        while (sayı >= 1):
            faktoriyel = faktoriyel * sayı
            sayı = sayı - 1
        print("Faktoriyel= ", faktoriyel)
    
faktoriyel(5)
faktoriyel(6)