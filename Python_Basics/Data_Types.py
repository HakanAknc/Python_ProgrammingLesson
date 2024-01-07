"""
* Python Data Types
Numeric - int, float, complex
String - str
Sequence - list, tuple, range
Binary - bytes, bytearray, memoryview
Mapping - dict
Boolean - bool
Set - set, frozenset
None - NoneType
"""

# var1 = 1       # int data type
# var2 = True    # bool data type
# var3 = 10.023  # float data type
# var4 = 10+3j   # complex data type

# print(type(5+6j))

# ****************************************
"""
# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))

# boolean variable.
b=True
print("The type of variable having value", b, " is ", type(b))

# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))
"""

# ? Python String Data Type

str = "Hakan Akıncı"

# print(str)
# print(str[0])
# print(str[2:5])  # 2'yi alır 5'i almaz
# print(str[2:7])
# print(str[:5])  # baştan istedğin yere kadar alır
# print(str[6:])  # sondan istediğin yere kadar alır
# print(str * 2)  # iki kere yazar
# print(str + "TEST")  # üzerine ekler
# print(str[:-6])
# print(str[-6:])


# ? Python List Data Type

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

# print (list)            # Prints complete list
# print (list[0])         # Prints first element of the list
# print (list[1:3])       # Prints elements starting from 2nd till 3rd 
# print (list[2:])        # Prints elements starting from 3rd element
# print (tinylist * 2)    # Prints list two times
# print (list + tinylist) # Prints concatenated lists


# ? Python Tuple Data Type
# Ancak listelerden farklı olarak, demetler parantez (...) içine alınır.

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

# print (tuple)               # Prints the complete tuple
# print (tuple[0])            # Prints first element of the tuple
# print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
# print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
# print (tinytuple * 2)       # Prints the contents of the tuple twice
# print (tuple + tinytuple)   # Prints concatenated tuples


# ? Python Ranges Function
# Python range(), Python'da 0'dan başlayarak belirli bir sayıya ulaşana kadar 
# 1'e kadar artan bir sayı dizisi döndüren yerleşik bir işlevdir

# range(start, stop, step)
"""
* start : Başlangıç ​​konumunu belirtmek için tam sayı, (İsteğe bağlı, Varsayılan: 0)
* stop : Başlangıç ​​konumunu belirtmek için tam sayı (Zorunlu)
* step : Artışı belirtmek için tam sayı, (İsteğe bağlı, Varsayılan: 1)
"""

# for i in range(5):
#     print(i)

# for i in range(1,5):
#     print(i)

# for i in range(1,5,2):
#     print(i)

# for i in range(-5,5):
#     print(i)



# ? Python Dictionary Data Type
# a= {1:"one", 2:"two", 3:"three"}
# print(a)

dict = {}
dict["one"] = "This is one"
dict[2]     = "This is two"

newdict = {"name": "jhon", "code": 4563, "dept": "sales"}

# print(dict["one"])
# print(dict[2])
# print (newdict)          # Prints complete dictionary
# print (newdict.keys())   # Prints all the keys
# print (newdict.values()) # Prints all the values


# ? Python Set Data Type
#  Python'da bir küme bir koleksiyondur


# ? Python Boolean Data Types
# ! True'nun 1'e ve False'ın 0'a eşit olduğunu unutmayın

# Returns false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)

# Returns False as a is None
a = None
print(bool(a))

# Returns false as a is an empty sequence
a = ()
print(bool(a))

# Returns false as a is 0
a = 0.0
print(bool(a))

# Returns false as a is 10
a = 10
print(bool(a))