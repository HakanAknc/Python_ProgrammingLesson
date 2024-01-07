
# ? Append() Yöntemi
# Append() yöntemi, verilen dizinin sonuna yeni bir öğe ekler.

import array as arr
a = arr.array('i', [1, 2, 3])
a.append(10)
print (a)

print()


# ? insert() Method
# Dizi sınıfı ayrıca insert() yöntemini de tanımlar. Belirtilen dizine yeni bir öğe eklemek mümkündür.

"""
array.insert(i, v)

i : Yeni değerin ekleneceği dizin.
v : Eklenecek değer. Dizi türünde olmalıdır.
"""

import array as arr
a = arr.array('i', [1, 2, 3])
a.insert(1,20)
print (a)

print()

# ? extend() Method
# Dizi sınıfındaki extend() yöntemi, aynı tür kodundaki başka bir dizideki tüm öğeleri ekler.

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
b = arr.array('i', [6,7,8,9,10])
a.extend(b)
print (a)