list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]

print ("Item at 0th index in list1: ", list1[0]) 
print ("Item at index 2 in list2: ", list2[2])  # index 0'dan başlar

print()

# Örnek negatif
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Item at 0th index in list1: ", list1[-1])
print ("Item at index 2 in list2: ", list2[-3])

print()

# Örnek
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Items from index 1 to 2 in list1: ", list1[1:3]) # ilk değer 1 için b'yi alır ama son değer 3 için bir öncesini alır yani b (b,c)
print ("Items from index 0 to 1 in list2: ", list2[0:2]) # ilk değeri alır 25.5 son değer için de True alır (25.5, True)

print()

list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]
list4 = ["Rohan", "Physics", 21, 69.75]
list3 = [1, 2, 3, 4, 5]

print ("Items from index 1 to last in list1: ", list1[1:]) # 1.indisden başlar sona kadar
print ("Items from index 0 to 1 in list2: ", list2[:2])  # 2.indis den öncekileri alır
print ("Items from index 2 to last in list3", list3[2:-2])
print ("Items from index 0 to index last in list4", list4[:]) # hepsini alır



