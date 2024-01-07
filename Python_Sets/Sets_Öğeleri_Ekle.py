
# ? add() Method
# Set sınıfındaki add() yöntemi yeni bir öğe ekler.
# Eğer eleman kümede zaten mevcutsa kümede herhangi bir değişiklik olmaz.


# Örnek
lang1 = {"C", "C++", "Java", "Python"}
lang1.add("Golang")
print (lang1)

print()

# ? update() Method

lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang1.update(lang2)
print (lang1)

print()

lang1 = {"C", "C++", "Java", "Python"}
lang2 = ("PHP", "C#", "Perl")
lang1.update(lang2)
print (lang1)

print()

set1 = set("Hello")
set1.update("World")
print(set1)


# ? union() Method

lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang3 = lang1.union(lang2)
print (lang3)

print()

lang1 = {"C", "C++", "Java", "Python"}
lang2 = ["PHP", "C#", "Perl"]
lang3 = lang1.union(lang2)
print (lang3)