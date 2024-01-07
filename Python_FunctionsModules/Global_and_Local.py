"""
def fonk():
    a = 5
    print(a)
fonk()
"""

"""
def fonk():
    a = 5
    print(a)
fonk()
print("a'nın değeri: ",a)
"""

"""
a = 10
def fonk():
    a = 5
    print(a)

fonk()
print("a'nın değeri: ",a)
"""

"""
def fonk():
    global a
    a = 5
    print(a)

fonk()
print("a'nın değeri: ",a)
"""

"""
a = 10
def fonk():
    a = 5
    return a
print("a'nın fonksiyon içindeki değeri: ",fonk())
print("a'nın fonksiyon dışındaki değeri: ",a)
"""


c = 10 # Globalde tanımlanmış bir değişken 
def fonksiyon():
    c = 2 # Yerelde tanımlanmış bir değişken
    print(c)  # Yerel değişken kullanılıyor.

fonksiyon()
print(c)

