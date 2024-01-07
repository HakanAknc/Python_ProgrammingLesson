# Belirli bir dizideki sesli harflerin sayısını bulan Python programı.

cümle = "Bugün hava açok güneşli ve sıcak"
sesli = "aeiıoöuü"
sayac = 0
for i in cümle:
    if i.lower() in sesli:
        sayac += 1
print("Sesli Harf Sayısı:",sayac)

print()

# Bir dizedeki tüm rakamları bırakan Python programı.

digits = [str(x) for x in range(10)]
mystr = 'He12llo, Py00th55on!'
chars = []
for x in mystr:
   if x not in digits:
      chars.append(x)
newstr = ''.join(chars)
print (newstr)

# İkili basamaklı bir dizeyi tam sayıya dönüştüren Python programı.

mystr = '10101'

def strtoint(mystr):
   for x in mystr:
      if x not in '01': return "Error. String with non-binary characters"
   num = int(mystr, 2)
   return num
print ("binary:{} integer: {}".format(mystr,strtoint(mystr)))