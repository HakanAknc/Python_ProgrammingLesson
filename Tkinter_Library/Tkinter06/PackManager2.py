import tkinter as tk

pencere = tk.Tk()
pencere.title("Uygulamaya Hoşgeldiniz :) ")
pencere.geometry("600x450")

buton_sol_1 = tk.Button(pencere, text="Buton1", fg="red")
buton_sol_1.pack(side=tk.LEFT)  # Butonu sol tarafa side parametresine tk.LEFT'i eşitleyerek koyduk.

buton_sol_2 = tk.Button(pencere, text="Buton2", fg="red")
buton_sol_2.pack(side=tk.LEFT)

buton_ust_1 = tk.Button(pencere, text="Buton3", fg="red")
buton_ust_1.pack(side=tk.TOP)  # Butonu üst tarafa side parametresine tk.TOP'ı eşitleyerek koyduk

buton_ust_2 = tk.Button(pencere, text="Buton4", fg="orange")
buton_ust_2.pack(side=tk.TOP)

buton_alt_1 = tk.Button(pencere, text="Buton5", fg="blue")
buton_alt_1.pack(side=tk.BOTTOM)   # Butonu alt tarafa side parametresine tk.BOTTOM'ı eşitleyerek koyduk.

buton_alt_2 = tk.Button(pencere, text="Buton6", fg="green", bg="gray")
buton_alt_2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)  #fill parametresini tk.BOTH'a; expand parametresini True'ya eşitleyelim. Ne kadar uzadığını görmek için de arka plan rengini değiştirelim.



pencere.mainloop()