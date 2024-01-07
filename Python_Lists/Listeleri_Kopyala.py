# lst1 = lst.copy()

lst = [10, 20]
lst1 = lst.copy()
print ("lst:", lst, "id(lst):",id(lst))
print ("lst1:", lst1, "id(lst1):",id(lst1))

print()

lst[0]=100
print ("lst:", lst, "id(lst):",id(lst))
print ("lst1:", lst1, "id(lst1):",id(lst1))


"""
liste.append(obj)               --> Nesne nesnesini listeye ekler

liste.clear()                   --> Listenin içeriğini temizler

liste.kopya()                   --> Liste nesnesinin bir kopyasını döndürür

liste.count(obj)                --> Obj'nin listede kaç kez oluştuğunun sayısını döndürür

list.extend(sıra)               --> Sıranın içeriğini listeye ekler

liste.index(obj)                --> Obj'nin göründüğü listedeki en düşük dizini döndürür

list.insert(indeks, nesne)      --> Obj nesnesini ofset indeksindeki listeye ekler

list.pop(obj=liste[-1])         --> Listedeki son nesneyi veya nesneyi kaldırır ve döndürür

list.remove(obj)                --> Obj nesnesini listeden kaldırır

liste.reverse()                 --> Listenin nesnelerini yerinde tersine çevirir

liste.sort([işlev])             --> Listedeki nesneleri sıralar, verilmişse karşılaştırma işlevini kullanın
"""