"""
def selamla():
    print("Merhaba benim adım hakan")
selamla()
"""

# ! İlk parametreli fonksiyon
"""
def selamla(isim):
    print("Merhaba, benim adım", isim)
selamla("Hakan")
selamla("Evren")
"""

"""
!Fonksiyon (tanımlanırken) parantez içinde belirtilen değerlere (parametre) adı verilir.
?Aynı fonksiyon (çağırılırken) parantez içinde belirtilen değerlere ise (argüman) adı verilir.
"""

# adım 1
"""
sayilar = [45, 90, 43]
print(sum(sayilar))
"""

# adım 2
"""
sayilar = [45, 90, 43]
a = 1
for i in sayilar:
    a = a * i

print(a)
"""

# adım 3
sayilar = [3,5,7]
def carp(liste):
    a = 1
    for i in liste:
        a = a * i
    print(a)

carp(sayilar)