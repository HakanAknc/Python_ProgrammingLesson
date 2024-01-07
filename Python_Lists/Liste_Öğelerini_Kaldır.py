"""
Liste sınıfı yöntemleri remove() ve pop() her ikisi de bir öğeyi listeden kaldırabilir.
! Aralarındaki fark,
Remove() işlevinin argüman olarak verilen nesneyi kaldırması,
pop() yönteminin ise verilen dizindeki bir öğeyi kaldırmasıdır.
"""

# ? remove() Yöntemini Kullanma
# ! remove() ile sayı vererek listeden silme işlemi yapılmaz

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics")
print ("List after removing: ", list1)

print()


# ? pop() Yöntemini Kullanma
# ! pop() ile isim vererek listeden silme işlemi yapılmaz

list2 = ["Rohan", 25.50, True, -55, 1+2j]
print ("Original list: ", list2)
list2.pop(2)
print ("List after popping: ", list2)


"""
!!! ÖNEMLİ !!!
? bir listenin en sonuna nasıl öğe ekleyeceğimizi = append()
* bir listenin herhangi bir yerine nasıl öğe ekleyeceğimizi = insert()
? listeden isim vererek nasıl öğe çıkaracağımızı = remove()
* listeden sayı vererek nasıl öğe çıkaracığımızı = pop()
"""


# ? "del" Anahtar kelime
# Python'da "del" Bellekten herhangi bir Python nesnesini silen anahtar kelime.

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
del list1[2]
print ("List after deleting: ", list1)