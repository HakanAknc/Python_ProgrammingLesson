"""
* Python Değişkenleri - Adlandırma Kuralı

! Değişken adı bir harfle veya alt çizgi karakteriyle başlamalıdır
! Değişken adı bir sayıyla veya $, (, * % vb. gibi herhangi bir özel karakterle başlayamaz.
! Değişken adı yalnızca alfasayısal karakterler ve alt çizgiler içerebilir (Az, 0-9 ve _ )
! Python değişken adları büyük/küçük harfe duyarlıdır; bu, Ad ve İSİM'in Python'da iki farklı değişken olduğu anlamına gelir.
! Değişkeni adlandırmak için Python'a ayrılmış anahtar sözcükler kullanılamaz.
"""

"""
* Değişkenin adı birden fazla kelime içeriyorsa bu adlandırma kalıplarını kullanmalıyız

? Camel case -> İlk harf küçük harftir, ancak sonraki her kelimenin ilk harfi büyük harftir. Örneğin: kmPerSaat, fiyatPerLitre
? Pascal case -> Her kelimenin ilk harfi büyük harftir. Örneğin: KmPerHour, PricePerLitre
? Snake case -> Kelimeleri ayırmak için tek alt çizgi (_) karakterini kullanın. Örneğin: saat başına km_başına, litre başına fiyat_başına
-
"""


"""
a = 100       # integer
b = 10.0      # float
c = "Hakan"   # string

print(a)
print(b)
print(c)
"""


"""
# a=10
# b=10
# c=10

a=b=c=10
print(a,b,c)
"""

# Aşağıda geçersiz Python değişken adları verilmiştir:

# 1counter = 100
# $_count  = 100
# zara-salary = 100000

# print (1counter)
# print ($count)
# print (zara-salary)