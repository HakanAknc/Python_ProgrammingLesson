
# ? array.reverse() Method
# Dizi türleri gibi dizi sınıfı da öğeleri ters sırada yeniden düzenleyen revers() yöntemini destekler.

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
a.reverse()
print (a)

print()


# ? array.count() Method
# Count() yöntemi, belirli bir öğenin dizide kaç kez oluştuğunu döndürür.

import array as arr
a = arr.array('i', [1, 2, 3, 2, 5, 6, 2, 9])
c = a.count(2)
print ("Count of 2:", c)

print()


# ? array.index() method
# Dizi sınıfındaki index() yöntemi, dizideki belirli bir öğenin ilk oluşumunun konumunu bulur.

a = arr.array('i', [1, 2, 3, 2, 5, 6, 2, 9])
c = a.index(2)
print ("index of 2:", c)

print()


