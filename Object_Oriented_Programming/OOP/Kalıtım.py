
# * Kalıtım (Inheritance)
# Bu konuda Nesne Tabanlı Programlamadaki inheritance(kalıtım veya miras alma) konseptini öğrenmeye çalışacağız. 
# Inheritance veya kalıtım bir sınıfın başka bir sınıftan özelliklerini(attribute ) ve metodlarını miras almasıdır.

# !Peki inheritance nerede işimize yarar ?

class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgilerigöster(self):

        print("Çalışan sınıfının bilgileri.....")

        print("İsim: {}  \nMaaş: {}  \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman
        

# Çalışan sınıfını oluşturduk şimdi de Yönetici sınıfını bu Çalışan sınıfından türetmeye çalışalım.

class Yönetici(Çalışan):  # ? Çalışan sınıfından miras alıyoruz.
    #pass # Pass Deyimi bir bloğu sonradan tanımlamak istediğimizde kullanılan bir deyimdir.
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı

"""
Burada, yönetici sınıfında herhangi bir şey tanımlamadık ancak 
Çalışan sınıfından bütün özellikleri ve metodları miras aldık. 
Bakalım burada Çalışan sınıfının metodlarını kullanabilecek miyiz ?
"""

# yönetici1 = Yönetici("Mehmet Baltacı",3000,"İnsan Kaynakları") # yönetici objesi

# yönetici1.bilgilerigöster()

# print()

# yönetici1.departman_degistir("Halka İlişkiler")
# print()

# yönetici1.bilgilerigöster()

yönetici2 = Yönetici("Mustafa Murat Coşkun",3000,"Bilişim") # yönetici objesi

yönetici2.bilgilerigöster()
print()

yönetici2.zam_yap(500)
print()

yönetici2.bilgilerigöster()

