# Belirli bir listedeki benzersiz sayıları bulmak için Python programı.

L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []
for i in L1:
    if i not in L2:
        L2.append(i)
print(L2)

print()


# Bir listedeki tüm sayıların toplamını bulan Python programı.

L1 = [1, 9, 1, 6, 3, 4]
ttl = 0
for x in L1:
   ttl+=x
print ("Sum of all numbers Using loop:", ttl)
ttl = sum(L1)
print ("Sum of all numbers sum() function:", ttl)

print()


# Python programı 5 rastgele tamsayıdan oluşan bir liste oluşturur.

import random
L1 = []
for i in range(5):
    x = random.randint(0, 100)
    L1.append(x)
print(L1)