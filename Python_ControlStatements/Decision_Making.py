"""
Karar Verme:
Python'un karar verme işlevi anahtar kelimelerinde gizlidir - if..elif...else . 
If anahtar sözcüğü bir boole ifadesi ve ardından iki nokta üst üste simgesi gerektirir.

İki nokta üst üste (:) sembolü girintili bir blok başlatır. Aynı girinti düzeyine sahip ifadeler, if ifadesindeki boole ifadesi True ise yürütülür . 
İfade Doğru (Yanlış) değilse, yorumlayıcı girintili bloğu atlar ve ifadeleri daha önceki girinti düzeyinde yürütmeye devam eder.
"""

# Örnek
# Alışveriş tutarı > 1000 ise %10 indirim hakkına sahip bir müşteri örneğini ele alalım; aksi takdirde indirim uygulanmaz. 
# Aşağıdaki akış şeması tüm karar verme sürecini göstermektedir.

indirim = 0
tutar = 1200

if tutar > 1000:
    indirim = tutar * 10 / 100

print("Toplam tutar = ", tutar - indirim)