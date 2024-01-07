var = "HELLO PYTHON"

print(var[0])   #H
print(var[7])   #Y
print(var[11])  #N
# print(var[12])  #hata verir

print()

print(var[-1]) #N
print(var[-5]) #Y
print(var[-12]) #H
# print(var[-13]) #hata verir

print()

print(var[0], var[-12])
print(var[7], var[-5])

print()
# Stringler değişmez bir nesnedir.
"""
var="HELLO PYTHON"
var[7]="y"
print (var)
"""

var1="HELLO PYTHON"

print ("var:",var1)
print ("var[3:8]:", var1[3:8]) # 3'ü alır ama 8'i almaz

print()

var2="HELLO PYTHON"
print ("var:",var2)
print ("var[0:5]:", var2[0:5])
print ("var[:5]:", var2[:5])  # baştan başlar belirtilen yerin bir eksiğine kadar alır

print()

var3="HELLO PYTHON"
print ("var:",var3)
print ("var[6:12]:", var3[6:12])
print ("var[6:]:", var3[6:])  # belirtilen yerden sona kadar alır

