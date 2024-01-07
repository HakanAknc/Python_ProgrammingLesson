# Sets == Kümeleme  == {}

# Örnek
s1 = {"Rohan", "Physics", 21, 69.75}
s2 = {1, 2, 3, 4, 5}
s3 = {"a", "b", "c", "d"}
s4 = {25.50, True, -55, 1+2j}
print (s1)
print (s2)
print (s3)
print (s4)

print()
print()

# set() işlevi, dizideki tekrarlanan öğeleri atarak diziden bir ayar nesnesi döndürür.

L1 = ["Rohan", "Physics", 21, 69.75]
s1 = set(L1)
T1 = (1, 2, 3, 4, 5)
s2 = set(T1)
string = "TutorialsPoint"
s3 = set(string)

print (s1)
print (s2)
print (s3)

print()


s2 = {1, 2, 3, 4, 5, 3,0, 1, 9}
s3 = {"a", "b", "c", "d", "b", "e", "a"}
print (s2)
print (s3)


# !!! Önemli
"""
Set bir sıra veri türü olmadığından, konumsal bir indekse sahip olmadıkları için 
(liste veya tuple'da olduğu gibi) öğelerine ayrı ayrı erişilemez.
"""