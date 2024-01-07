"""
* continue
- belirlenen şartı atlar devam eder
-Continue ifadesi hem while hem de for döngülerinde kullanılabilir .
"""

"""
for evren in "Python":
    if evren == "h":
        continue
    print("Harfler :", evren)
print()

var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print("Sayılar :", var)
print("Görüşürüz...")
"""


# Asal Faktörlerin Kontrol Edilmesi

num = 75
print("Bu sayını için: ", num)
d=2
while num > 1:
    if num%d==0:
        print(d)
        num=num/d
        continue
    d=d+1

print()

for i in range(1,11):
    if i == 6:
        continue
    else:
        print(i, end=" ")