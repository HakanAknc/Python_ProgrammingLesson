"""
Mevcut bir listeye öğe eklemek için kullanılan 
list sınıfının Append() ve Insert() adlı iki yöntemi vardır. .
"""

# ? append() yöntemi, öğeyi mevcut bir listenin sonuna ekler.
# Listeden bir şey kaldırmaz ekler

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list1.append('e')
print ("List after appending: ", list1)

print()


# ? insert() yöntemi, öğeyi listede belirtilen bir dizine ekler.
# Listeden bir şey kaldırmaz ekler

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list ", list1)

list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)

list1.insert(-1, 'Pass')
print ("List after appending: ", list1)