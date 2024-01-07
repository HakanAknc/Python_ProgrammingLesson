import tkinter as tk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoşgeldiniz.")

def butonFonksiyonu():
    # print("Butona tıkaldın...")

    etiket.config(
        text="Değiştim",
        bg="red",
        font="Verdana"
    )

buton = tk.Button(
    pencere,
    text="Ben bir butonum",
    bg="yellow",
    fg="red",
    activebackground="blue",
    activeforeground="white",
    font=25,
    height=5,
    width=20,
    cursor="hand2",
    command=butonFonksiyonu
)

buton.pack()

etiket = tk.Label(
    pencere,  # pencere, butonun ekleneceği yerdir.
    text="Ben bir etiketim",  # etiketin üzerinde görünecek metni belirtir.
    font="Tahoma 24", # metnin kullanacağı yazı tipini ve boyutunu belirtir.
    bg="blue",   # tiketin arka plan rengini belirtir. 
    fg="white",   # etiketin metin rengini belirtir.
    wraplength=150,  # wraplength, etiketin kaç piksel genişliğinde bir hizada sarma yapması gerektiğini belirtir.
    #pady=30,  # dikey bir şekilde büyütür
    #padx=50  # yatay bir şekilde büyütür
)

etiket.pack(pady=15)  # kutular arasında boşluk bıraktı
#etiket.pack()

pencere.mainloop()