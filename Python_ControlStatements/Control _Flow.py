"""
Varsayılan olarak, bir bilgisayar programındaki talimatlar yukarıdan aşağıya veya baştan sona sıralı bir şekilde yürütülür. 
 bu tür sıralı olarak çalıştırılan programlar yalnızca basit görevleri gerçekleştirebilir.
"""

"""
! Kontrol 
? if..elif..else
? Case
? For
? While
"""

# * if..elif..else
marks = 80
result = ""
if marks < 30:
    result = "Faild"
elif marks > 75:
    result = "Passed with distinction"
else:
    result = "Passed"

print(result)

print("***************************")


# * Case
def checkVowel(n):
   match n:
      case 'a': 
         return "Vowel alphabet"
      case 'e': 
         return "Vowel alphabet"
      case 'i': 
         return "Vowel alphabet"
      case 'o': 
         return "Vowel alphabet"
      case 'u': 
         return "Vowel alphabet"
      case _: 
         return "Simple alphabet"
      
print (checkVowel('a'))
print (checkVowel('m'))
print (checkVowel('o'))

print("**************************")


# * For
words = ["one","two","three"]
for x in words:
   print(x)

print("**************************")


# * While
i = 1
while i < 6:
   print(i)
   i += 1