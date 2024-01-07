# Örnek1
lst = [25, 12, 10, -21, 10, 100]
for num in lst:
    print(num, end=" / ")  # end araya istedğimiz değeri koydurur.

print()
print()

lst = [25, 12, 10, -21, 10, 100]
indices = range(len(lst))
# print(indices)
for i in indices:
    print("lst[{}]: ".format(i), lst[i])

print()
print()

liste = []
for lste in "TutorialsPoint":
    if lste not in "aeiou":
        liste.append(lste)
print(liste)