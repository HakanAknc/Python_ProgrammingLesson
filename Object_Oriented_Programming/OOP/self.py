
# class Araba():
#     model = "Renault Megane"
#     renk = "Gümüş"             # Sınıfımızın özellikleri (attributes)
#     beygir_gücü = 110
#     silindir = 4


# araba1 = Araba()
# araba2 = Araba()


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

class Araba():

    def __init__(self,model,renk,beygir_gücü,silindir): # Parametrelerimizin değerlerini objelerimizi oluştururken göndereceğiz.
        self.model =  model # self.özellik_ismi = parametre değeri şeklinde objemizin model özelliğine değeri atıyoruz.
        self.renk = renk # self.özellik_ismi = parametre değeri şeklinde objemizin renk özelliğine değeri atıyoruz.
        self.beygir_gücü = beygir_gücü # self.özellik_ismi = parametre değeri şeklinde objemizin beygir_gücü özelliğine değeri atıyoruz.
        self.silindir = silindir # self.özellik_ismi = parametre değeri şeklinde objemizin silndir özell
        self.silindir = silindir # self.özellik_ismi = parametre değeri şeklinde objemizin silndir özelliğine değeri atıyoruz.

# araba1 objesini oluşturalım.
# Artık değerlerimizi göndererek objelerimizin özelliklerini istediğimiz değerle başlatabiliriz.

araba1 = Araba("Peugeot 301","Beyaz",90,4)

# araba2 objesini oluşturalım.
araba2 = Araba("Renaul Megane","Gümüş",110,4)

print(araba1.model)
print(araba1.renk)
print()
print(araba2.model)
print(araba2.renk)
print()


# ? İstersek init metodunu varsayılan değerlerle de yazabiliriz.

class Araba():
    
    def __init__(self , model = "Bilgi Yok",renk = "Bilgi Yok",beygir_gücü = 75 ,silindir = 4): 
        self.model =  model 
        self.renk = renk 
        self.beygir_gücü = beygir_gücü 
        self.silindir = silindir

araba1 = Araba(beygir_gücü = 85, renk = "Siyah")
print(araba1.renk)
print(araba1.model)

# İşte burada gördüğümüz gibi bir objeyi init metodunu kendimiz yazarak farklı değerlerle oluşturabiliyoruz.