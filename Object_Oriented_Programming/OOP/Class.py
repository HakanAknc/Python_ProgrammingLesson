# Nesne Tabanlı Programlama

# ! Class
# Sınıflar veya Classlar objelerimizi oluştururken objelerin özelliklerini ve
# metodlarını tanımladığımız bir yapıdır ve biz herbir objeyi bu yapıya göre üretiriz.

# Yeni bir Araba veri tipi oluşturuyoruz.
class Araba():
    model = "Renault Megane"
    renk = "Gümüş"             # Sınıfımızın özellikleri (attributes)
    beygir_gücü = 110
    silindir = 4

# Sınıfımızı Pythonda tanımladık. Peki bu sınıftan obje nasıl oluşturacağız ? Bunu da şu şekilde yapabiliyoruz.

"""
-------------------------------------------------------------------

     obje_ismi = Sınıf_İsmi(parametreler(opsiyonel))

-------------------------------------------------------------------
"""

araba1 = Araba()   # Araba veri tipinde bir "araba1" isiminde bir obje oluşturduk.
araba1 # Objemizin veri tipi Araba
type(araba1)

#araba1 objesi artık sınıfta tanımladığımız bütün özelliklere (attributes) sahip olmuş oldu. 
#İşte sınıf ve obje üretmek bu şekilde olmaktadır. 
#Peki bu araba objesinin özelliklerinin nasıl görebiliriz ?

"""
-------------------------------------------

        obje_ismi.özellik_ismi
-------------------------------------------
"""

print(araba1.model)  #'Renault Megane'
print(araba1.renk)  #'Gümüş'
print(araba1.beygir_gücü)  #110
print(araba1.silindir)  #4

print()

# Şimdi de başka bir Araba objesi oluşturalım.

araba2 = Araba()

print(araba2.model)  #'Renault Megane'
print(araba2.renk)   #'Gümüş'
print(araba2.beygir_gücü)  #100
print(araba2.silindir)     #4

print()

## Class_İsmi.özellik_ismi
print(Araba.renk)
print(Araba.beygir_gücü)

print()

"""
Bizim her bir objeyi başlangıçta farklı değerlerle oluşturmamız için 
her bir objeyi oluştururken objelerin değerlerini göndermemiz gerekiyor. 
Bunun için de özel bir metodu kullanmamız gerekmektedir. 
---------------------------- init() -------------------------------------
"""

#Peki bu metod ne anlama geliyor ? 
#İsterseniz ilk olarak *dir()* fonksiyonu yardımıyla araba1 objemizde neler var bakalım.

# print(dir(araba1))

# ? ---------------------------- init() -------------------------------------
# * Aslında init metodu Pythonda yapıcı(constructor ) fonksiyon olarak tanımlanmaktadır.
# * Bu metod objelerimiz oluşturulurken otomatik olarak ilk çağrılan fonksiyondur.
# * Bu metodu özel olarak tanımlayarak objelerimizi farklı değerlerle oluşturabiliriz.

# Araba veri tipi

class Araba():
    # Şimdilik class özelliklerine ihtiyacımız yok

    def __init__(self):
        print("İnit fonksiyonu çağırıldı.")

araba1 = Araba()  ## araba1 objesi oluşurken otomatik olarak __init__ metodumuz çağrılıyor

print()

# ! Peki burada self ne anlama geliyor ?
"""
self anahtar kelimesi objeyi oluşturduğumuz zaman 
o objeyi gösteren bir referanstır ve metodlarımızda
en başta bulunması gereken bir parametredir.
Yani biz bir objenin bütün özelliklerini ve metodlarını bu referans üzerinden kullanabiliriz.
"""

# ?Objeler oluşturulurken, Python bu referansı metodlara otomatik olarak kendisi gönderir. 
# ?Özel olarak self referansını göndermemize gerek yoktur.

# init metodunu ve self'i iyi anlamak için objelerimize özellikler ekleyelim.
