"""
import array
obj = array.array(typecode[, initializer])

typecode : Diziyi oluşturmak için kullanılan tür kodu karakteri.
initializer : isteğe bağlı değerden başlatılan dizi; bu bir liste, bayt benzeri bir nesne veya uygun türdeki öğeler üzerinde yinelenebilir olmalıdır.
"""

# array() yapıcısı array.array sınıfının bir nesnesini döndürür

import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print (type(a), a)

# creating an array with char type
a = arr.array('u', 'BAT')
print (type(a), a)

# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)