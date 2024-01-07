import tkinter as tk

form = tk.Tk()
form.title("Tkinter Dersleri-1")  # başlık
  
etiket = tk.Label(text="Tkiner Python")
etiket.pack()   #pack ekrana yazdırır yazdırır

etiket2 = tk.Label(form,text="Hakan Akıncı")
etiket2.pack()

form.mainloop()