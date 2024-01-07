import tkinter as tk

pencere = tk.Tk()

pencere.geometry("650x450")
pencere.title("Uygulamaya Hoş gelddinzi.")

def butonFonksiyonu():
    print("Butona tıkladın...")

button = tk.Button(
    pencere,   # pencere, butonun ekleneceği yerdir.
    text="Ben bir buttonum",  # text, butonun üzerinde görünecek metindir
    bg="orange",  # bg, butonun arka plan rengidir.
    fg="black",   # fg, butonun metin rengidir.
    activebackground="red",  # butona tıklanıldığında dönüşecek olan arka plan rengidir.
    activeforeground="white",  # butona tıklanıldığında değişecek olan metin rengidir. 
    font=24,  # font, butonun metin fontudur.
    height=5,  # height, butonun yüksekliğidir
    width=20,  # width, butonun genişliğidir.
    cursor="hand2",  # cursor, butonun üzerine gelindiğinde imlecin nasıl değişeceğidir.
    command=butonFonksiyonu  # command, buton tıklandığında çalışacak olan fonksiyondur. Bu fonksiyonun ismi "butonFonksiyonu"dur.
)

button.pack()

pencere.mainloop()