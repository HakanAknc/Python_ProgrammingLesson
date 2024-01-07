import tkinter as tk
from tkinter import messagebox

pencere = tk.Tk()

pencere.geometry("600x450")
pencere.title("Uygulamaya Hoşgeldiniz :)")

def butonFonksiyon():
    #print("Butona tıkladın...")

    etiket.config(
        text="Nasılsın?",
        bg="red",
        font="Verdana"
    )

    yazdigin_sey = giris.get()
    etiket.config(text=yazdigin_sey)
    giris.config(state="disabled")

    mesaj = messagebox.showinfo(
        title="Bilgi",
        message="Butona tıkladın."
    )


buton = tk.Button(
    pencere,
    text="Ben bir butonum",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="white",
    font=24,
    height=5,
    width=20,
    cursor="hand2",
    command=butonFonksiyon
)

buton.pack()

etiket = tk.Label(
    pencere,
    text="Ben bir etiketim",
    font="Tahoma 24",
    bg="blue",
    fg="white",
    wraplength=150
)

etiket.pack(pady=10)

giris = tk.Entry(
    pencere,
    width=50  # width, giriş kutusunun genişliğidir.
)

giris.insert(
    string="Kafanıza göre bir şeyler yazınız...",
    index=0   # index'in ise 0 olması, metni giriş bileşeninin başlangıcına eklemektir.
)

giris.pack()


pencere.mainloop()