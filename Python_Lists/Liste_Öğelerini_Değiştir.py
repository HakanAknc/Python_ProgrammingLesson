# Örnek1
list3 = [1, 2, 3, 4, 5]
print ("Original list ", list3)
list3[2] = 10
print("Yeni liste: ", list3)

print()

# Örnek 2
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)

list2 = ['Y', 'Z']
list1[1:3] = list2  # 1.indis ile 2.indis yerine "Y" ve "Z" yaz
print ("List after changing with sublist: ", list1)

print()

# Örnek3
list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['X','Y', 'Z']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)