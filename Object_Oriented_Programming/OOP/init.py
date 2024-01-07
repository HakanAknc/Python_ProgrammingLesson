
class Araba():
    model = "Renault Megane"
    renk = "Gümüş"             # Sınıfımızın özellikleri (attributes)
    beygir_gücü = 110
    silindir = 4


araba1 = Araba()
araba2 = Araba()

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
