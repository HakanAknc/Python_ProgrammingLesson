import tkinter as tk

pencere = tk.Tk()
pencere.title("Uygulamaya Hoşgeldinzi")

etiket1 = tk.Label(pencere, text="Etiket1")
etiket1.place(x = 25, y = 25)

etiket2 = tk.Label(pencere, text="Etiket2")
etiket2.place(relx = 0.5, rely = 0.5)

pencere.mainloop()