"""
1- Syntax errors
2- logical errors
3- runtime errors
"""
# Dilin belirlediği kurallara uyulmadığı zaman Syntax errors hataları ortaya çıkar.

# Aşağıda Python etkileşimli kabuğunda bir değişken bildirmenin basit bir örneği verilmiştir.
"""
name="Python
   File "<stdin>", line 1
      name="Python
           ^
SyntaxError: unterminated string literal (detected at line 1)
"""

# Benzer şekilde Python, her işlev adının, içinde işlev argümanlarının verilmesi gereken parantezlerle takip edilmesini gerektirir.
# Aşağıdaki örnekte bir sözdizimi hatası alıyoruz –
"""
print "Hello"
   File "<stdin>", line 1
      print "Hello"
      ^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
"""
# Bunun nedeni, print() fonksiyonunda parantezlerin eksik olması hata mesajından anlaşılmaktadır.

# ! İSTİSNA
"""
object
   BaseException
      Exception
         ArithmeticError
            FloatingPointError
            OverflowError
            ZeroDivisionError
         AssertionError
         AttributeError
         BufferError
         EOFError
         ImportError
            ModuleNotFoundError
         LookupError
            IndexError
            KeyError
         MemoryError
         NameError
         OSError
         ReferenceError
         RuntimeError
         StopAsyncIteration
         StopIteration
         SyntaxError
"""