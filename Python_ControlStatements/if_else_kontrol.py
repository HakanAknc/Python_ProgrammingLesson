# Yaş kontrolü

# age = 25
# print("age: ", age)
# if age >= 18:
#     print("Oy kullanabilirsiniz.")
# else:
#     print("Oy kullanamazsınız.")
    

"""
# elif kullanımı
"""
#* örnek
# 10000'i aşan tutarda %20,
# 5-10000 arası miktar için %10,
# 1 ile 5000 arasında ise %5.
# tutar <1000 ise indirim yapılmaz
"""

# çözüm 1
değer = 10001
print("Değer: ", değer)
if değer > 10000:
    indirim = değer * 20 / 100
else:
    if değer > 5000:
        indirim = değer * 10 / 100
    else: 
        if değer > 1000:
            indirim = değer * 5 / 100
        else:
            indirim = 0

print("Toplam ödenecek değer = ", değer - indirim)

print("************************************")

# çözüm 2
amount = 2500
print("Amount = ", amount)
if amount > 10000:
    discount = amount * 20 / 100
elif amount > 5000:
    discount = amount * 10 / 100
elif amount > 1000:
    discount = amount * 5 / 100
else:
    discount = 0

print("Payable amount = ", amount - discount)
"""


# İç içe if elif kullanımı

num = 24
print("num = ", num)

if num%2==0:
    if num%3==0:
        print("2 ve 3 tam bölünüyor")
    else:
        print("2'ye bölünür 3'e bölünmez")
else:
    if num%3==0:
        print("3'e bölünür 2'ye bölünmez")
    else:
        print("2 ve 3 tam bölünmez")