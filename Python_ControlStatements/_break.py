"""
* break
-Geçerli döngüyü 
-Break ifadesi hem while hem de for döngülerinde kullanılabilir .
"""

for letter in "Python":
    if letter == "h":
        break
    print("Currnet Letter :", letter)
print("Bitti...")

var = 10
while var > 0:
    print("Current variable value :", var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")