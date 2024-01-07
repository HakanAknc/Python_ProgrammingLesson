class Yazılımcı():

    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.diller = diller
    
    #  Aynı init metodunu tanımladığımız gibi bir class'a da istediğimiz kadar metod tanımlayabiliriz.
    # Örneğin ,Yazılımcı classına bilgilerigöster isimli bir metod tanımlayalım.
    def bilgilerigöster(self):
        print("""
        Çalışan Bilgisi:
        
        İsim : {}
        
        Soyisim : {}
              
        Şirket Numarası : {}
              
        Maaş : {}
              
        Diller : {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    
    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor.")
        self.diller.append(yeni_dil)
        
    def maas_yukselt(slef,zam_miktarı):
        print("Maaş yükseliyor.")
        slef.maaş += 250 


# yazılımcı objesi
yazılımcı1 = Yazılımcı("Mustafa Murat","Coşkun",12345,3000,["Python","C","Java"])
# yazılımcı2 = Yazılımcı("Serhat","Say",23456,3500,["Matlab","R","SmallTalk"])

# print(yazılımcı1.diller)
# print(yazılımcı2.soyisim)

# yazılımcı1.bilgilerigöster()

# * Metodlarımızı yazarken dikkat etmemiz gerek nokta, her metodun birinci parametresinin self referansı olması gerektiğidir. 
# * Ayrıca objelerimizin özelliklerine mutlaka self referansıyla erişmemiz gerekiyor.

yazılımcı1.maas_yukselt(500)
print()

yazılımcı1.bilgilerigöster()

print()

yazılımcı1.dil_ekle("JavaScript")
print()

yazılımcı1.bilgilerigöster()