"""
Dizi sınıfı, diziden bir öğeyi kaldırabileceğimiz iki yöntemi tanımlar. Remove() ve pop() yöntemlerine sahiptir
"""

# ? array.remove() Method
# Remove() yöntemi, belirli bir değerin ilk oluşumunu diziden kaldırır
# index yok istediğin değeri çıkartır

import array as arr
a = arr.array('i', [1, 2, 1, 4, 2])
a.remove(2)
print (a)

print()


# ? array.pop() Method
# pop() yöntemi, belirtilen dizindeki bir öğeyi diziden kaldırır ve kaldırılan öğeyi döndürür.
# index var istediğin değerin index değeri ile çıkarılır

import array as arr
a = arr.array('i', [1, 2, 1, 4, 2])
a.pop(2)
print (a)