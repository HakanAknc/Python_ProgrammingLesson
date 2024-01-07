"""
Girintili bir ifade bloğu başlatmak için while anahtar sözcüğünden sonra bir boole ifadesi 
ve ardından iki nokta üst üste simgesi gelir

# while expression:
#    statement(s)
"""


"""
count=0
while count<5:
    count+=1
    print("Iteration no. {}".format(count))

print("End of while loop")
"""

"""
var = '0'
while var.isnumeric()==True:
    var=input('enter a number..')
    if var.isnumeric()==True:
        print("Your input",var)
print("End pf while loop")
"""

# Örnek 1: Python While Döngüsü
"""
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
"""

# Örnek 2: Listeli Python while döngüsü
"""
a = [1, 2, 3, 4]
while a:
    print(a.pop())   # pop() : tersten yazdırma
"""

# Örnek 3: Tek ifade while bloğu
"""
count = 0
while (count < 5): count += 1; print("Hello Geek")
"""


# Örnek 4: Döngü Kontrol İfadeleri
# ?Örnek: Continue ifadesi ile Python while döngüsü
"""
i=0
a="geeksforgeeks"

while i < len(a):
    if a[i] == "e" or a[i] == "s":
        i += 1
        continue

    print("Harfler :", a[i])
    i += 1
"""

# Örnek 5: Döngü Kontrol İfadeleri
# ?Örnek: Break ifadesi ile Python while 
"""
i = 0
a = 'geeksforgeeks'
 
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
         
    print('Current Letter :', a[i])
    i += 1
"""

# Örnek 6: Döngü Kontrol İfadeleri
# ?Örnek: Pass ifadesi ile Python while 
'''
a = 'geeksforgeeks'
i = 0

while i < len(a):
	i += 1
	pass

print('Value of i :', i)
'''


# while ile else döngüsü
"""
i = 0
while i < 4:
    i+=1
    print(i)
else:
    print("No Break\n")

i = 0
while i < 4:
    i+=1
    print(i)
    break
else:
    print("No Break")
"""


# Örnek: Boolean değerlerinde while döngüsü:
"""
count = 0

while True:
	count += 1
	print(f"Count is {count}")

	if count == 10:
		break

print("The loop has ended.")
"""
