"""
# Returnsuz:
def fonk(isim,yas):
    print("Merhaba ismim {}, {} yaşındayım memnun oldum".format(isim,yas))

fonk("Hakan",22)
"""

"""
# Return:
def fonk(isim,yas):
    return ("Merhaba ismim {}, {} yaşındayım memnun oldum.".format(isim,yas))

print(fonk("Hakan",24))
"""

"""
def meyverler(*meyve):
    print(meyve[0])
    print(meyve[1])
    print(meyve[5])

meyverler("elma","muz","çilek","kavun","armut","karpuz","kiraz","portakal")
"""

"""
def carpma(x,y):
    return x*y

print(carpma(7,5))

print("*****************")

def topla(a,b):
    print(a+b)

topla(5,10)

print("**************")

def selam(isim):
    return "Merhaba " +isim

print(selam("Hakan"))


print("*/**/*/*/*//*/*/*//*/+-+/*-+/")

def faktoriyel(x):
    if x == 1:
        return 1
    else:
        return x * faktoriyel(x-1)

print(faktoriyel(5))

print("***************************")

x = lambda a : a + 10
print(x(5))
"""

def fonksiyon(**parametreler):
    print(parametreler)
fonksiyon(isim="Ahmet", soyisim="Öz", meslek="Mühendis", şehir="Ankara")

print()

def kayıt_oluştur(isim, soyisim, işsis, şehir):
    print("-"*30)
    print("isim : ", isim)
    print("soyisim : ", soyisim)
    print("işletim sistemi: ", işsis)
    print("şehir : ", şehir)
    print("-"*30)
kayıt_oluştur("Hakan","Akıncı","Windos","Konya")