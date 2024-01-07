import array as arr
a = arr.array('i', [1, 2, 3])
#indexing
print (a[1])
#slicing
print (a[1:])

print()


# ? Dizi Öğelerini Değiştirme
# Listedeki bir öğeye değer atadığınız gibi, dizideki bir öğeye de değer atayabilirsiniz.

import array as arr
a = arr.array('i', [1, 2, 3])
a[1] = 20
print (a[1])