
# ? remove() Method
"""
Python'un set sınıfı, bir set nesnesinden bir veya daha fazla öğeyi 
kaldırmak için farklı yöntemler sağlar.
"""

# Örnek

lang1 = {"C", "C++", "Java", "Python"}
print ("Set before removing: ", lang1)
lang1.remove("Java")
print ("Set after removing: ", lang1)
lang1.remove("PHP")

print()

# ? discard() Method

lang1 = {"C", "C++", "Java", "Python"}
print ("Set before discarding C++: ", lang1)
lang1.discard("C++")
print ("Set after discarding C++: ", lang1)
print ("Set before discarding PHP: ", lang1)
lang1.discard("PHP")
print ("Set after discarding PHP: ", lang1)

print()


# ? pop() Method
#Set sınıfındaki pop() yöntemi, set koleksiyonundan rastgele bir öğeyi kaldırır.
#! kaldırır

# örnek
lang1 = {"C", "C++"}
print ("Set before popping: ", lang1)
obj = lang1.pop()
print ("object popped: ", obj)
print ("Set after popping: ", lang1)
obj = lang1.pop()
obj = lang1.pop()


# ? clear() Method
# Set sınıfındaki clear() yöntemi, bir set nesnesindeki tüm öğeleri kaldırarak boş bir set bırakır.

# örnek
lang1 = {"C", "C++", "Java", "Python"}
print (lang1)
print ("After clear() method")
lang1.clear()
print (lang1)