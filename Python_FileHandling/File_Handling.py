# Python'un dosyaları oluşturmak, okumak, güncellemek ve silmek için çeşitli işlevleri vardır.

# ? Dosya yönetimi
# Python'da dosyalarla çalışmanın temel işlevi işlevdir #! open().

"""
*Bir dosyayı açmak için dört farklı yöntem (mod) vardır:
"r" --> Okuma (Read)  ---> Varsayılan değer. Okumak için bir dosyayı açar, dosya mevcut değilse hata verir
"a" --> Ekle (Append) ---> Eklemek üzere bir dosyayı açar, mevcut değilse dosyayı oluşturur
"w" --> Yaz (Write)   ---> Bir dosyayı yazmak için açar, mevcut değilse dosyayı oluşturur
"x" --> Oluştur (Create) -> Belirtilen dosyayı oluşturur, dosya mevcutsa bir hata döndürür
"""
"""
* Ayrıca dosyanın ikili modda mı yoksa metin modunda mı işlenmesi gerektiğini belirleyebilirsiniz.
"t"- Metin (Text) - Varsayılan değer. Metin modu
"b"- İkili (Binary) - İkili mod (örn. görüntüler)
"""

# f = open("hakan.txt", "w")
# print(f)   # ? dosya oluşturduk

# f = open("hakanx.txt", "x")
# print(f)  # ? dosya oluşturur

# f = open("hakan.txt", "w")
# f.write("Merhaba ben Hakan Akinciiiii...")
# print(f)   # ? dosyaya yazar


# f = open("hakan.txt", "r")
# print(f.read())   # ? dosyayı okur

# f = open("hakan.txt", "r")
# print(f.readlines())   # ? dosyayı liste çıktısı verir.

# f = open("hakan.txt", "r")
# print(f.readline())   # ? dosyanın ilk satırını okur

# import os
# os.remove("hakanx.txt")   # ? dosyayı siler