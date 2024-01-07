import tkinter as tk
from tkinter import scrolledtext

class MessageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basit Mesajlaşma Uygulaması")

        # Mesajları göstermek için bir scrolled text alanı
        self.message_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.message_area.pack(padx=10, pady=10)

        # Mesaj girişi için bir Entry alanı
        self.message_entry = tk.Entry(root, width=30)
        self.message_entry.pack(padx=10, pady=10)

        # Gönderme butonu
        send_button = tk.Button(root, text="Gönder", command=self.send_message)
        send_button.pack(pady=5)

    def send_message(self):
        # Mesajı al
        message = self.message_entry.get()

        # Mesajı scrolled text alanına ekle
        self.message_area.insert(tk.END, f"You: {message}\n")

        # Mesaj girişini temizle
        self.message_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MessageApp(root)
    root.mainloop()
