import tkinter as tk

pencere = tk.Tk()
pencere.title("Uygulamaya Hoşgeldinzi.")

for satir in range(1,16):
    for sutun in range(1,11):
        etiket = tk.Label(pencere, text="Satır%s-Sütun%s"%(satir,sutun))
        etiket.grid(row=satir, column=sutun, padx=5, pady=5)

pencere.mainloop()