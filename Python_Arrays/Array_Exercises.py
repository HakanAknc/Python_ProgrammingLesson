# Örnek 1
# Bir dizideki en büyük sayıyı bulan Python programı –

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
largest = a[0]
for i in range(1, len(a)):
   if a[i]>largest:
      largest=a[i]
print ("Largest number:", largest)

print()


# Örnek 2
# Bir dizideki tüm çift sayıları başka bir dizide saklayan Python programı –

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
b = arr.array('i')
for i in range(len(a)):
   if a[i]%2 == 0:
      b.append(a[i])
print ("Even numbers:", b)

print()


# Örnek 3
# Bir Python dizisindeki tüm sayıların ortalamasını bulan Python programı –

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
s = 0
for i in range(len(a)):
   s+=a[i]
avg = s/len(a)
print ("Average:", avg)

# Using sum() function
avg = sum(a)/len(a)
print ("Average:", avg)

print()

