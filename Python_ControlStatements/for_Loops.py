# Bir Tuple ile "for" kullanımı
"""
numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0
for num in numbers:
    total+=num    # total = total(0) + num(34+54+67+....+19)
print("Total =", total)
"""


# Bir Listeyle "for" kullanımı
"""
numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
    if num%2 == 0:
        print(num)
"""


# Bir Range Nesnesiyle "for" kullanımı
"""
range(start, stop, step)
-Başlangıç ​​– Aralığın başlangıç ​​değeri. İsteğe bağlı. Varsayılan 0'dır
-Stop − Aralık stop-1'e kadar gider
-Adım – Aralıktaki tamsayılar adım değeri kadar artar. Seçenek, varsayılan 1'dir.
"""

numbers = range(5)
"""
start is 0 by default,
step is 1 by default,
range generated from 0 to 4
"""
"""
print(list(numbers))
print(tuple(numbers))

numbers = range(10,20)
print(list(numbers))

numbers = range(1, 10, 2)
print(list(numbers))
"""

for num in range(5):
    print(num, end=' ')
print()
for num in range(10,20):
    print(num, end=' ')
print()
for num in range(1, 10, 2):
    print(num, end=' ')
print("**************************************")


# Bir Sayının Faktöriyeli
"""
fact = 1
n = 5
for i in range(1, n+1):
    fact=fact*i
print("Faktöriyel {} = {}".format(n, fact))
"""


# Sıra İndeksi ile "for" Döngüsünü Kullanmak
"""
numbers = [34,54,67,21,78]
indices = range(len(numbers))
for index in indices:
    print("index:",index, "number:",numbers[index])
"""


# Sözlüklerde "for" kullanımı

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for i in numbers:
    print(i,":",numbers[i])