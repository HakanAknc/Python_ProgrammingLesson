import tkinter as tk

form = tk.Tk()
form.title("Tkinter Dersleri Formu")

label = tk.Label(form,text="Hakan Akıncı")
label.pack()

label2 = tk.Label(form,text="Python GIU",fg="red")
label2.pack()



form.mainloop()