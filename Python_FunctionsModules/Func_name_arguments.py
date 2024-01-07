"""
def kayit_ekle(isim, soyisim, sehir, meslek, tel, adres):
    kayit = {}
    kayit["%s %s" %(isim, soyisim)] = [sehir, meslek,
                                       tel, adres]
    
    print("Bağlantı bilgileri kayıtlara eklendi!\n")

    for k, v in kayit.items():
        print(k)
        print("-"*len(k))
        for i in v:
            print(i)

kayit_ekle("Hakan", "Akıncı",
           "Siirt", "Yazılımcı",
           "0542 543 56 36", "Meram/Köyceğiz")
"""

def kayit_ekle(isim, soyisim, sehir, meslek, tel, adres):
    kayit = {}
    kayit["%s %s" %(isim, soyisim)] = [sehir, meslek,
                                       tel, adres]
    
    print("Bağlantı bilgileri kayıtlara eklendi!\n")

    for k, v in kayit.items():
        print(k)
        print("-"*len(k))
        for i in v:
            print(i)

isi = input("İsim: ")
soy = input("Soyisim: ")
seh = input("Şehir: ")
mes = input("Meslek: ")
tel = input("Tel: ")
adr = input("Adres: ")

kayit_ekle(isi,soy,seh,mes,tel,adr)

# sozluk = {"programlama dili": "Python",
#           "Metin düzenletyici": "Kwrite"}

# print(sozluk.items())


# for k, v in sozluk.items():
#     print(k,v)