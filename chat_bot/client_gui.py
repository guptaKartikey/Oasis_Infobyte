import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

# GUI Client Class
class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Chat Client")

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, state='disabled', width=50, height=20)
        self.chat_area.pack(padx=10, pady=10)

        # Entry field
        self.entry = tk.Entry(master, width=40)
        self.entry.pack(side=tk.LEFT, padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, pady=10)

        # Network setup
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "127.0.0.1"   # Same as server
        port = 12345
        self.client_socket.connect((host, port))

        # Start receiving messages
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode()
                if not msg:
                    break
                self.display_message(msg)
            except:
                break

    def send_message(self, event=None):
        msg = self.entry.get()
        if msg.strip():
            self.client_socket.send(msg.encode())
            self.display_message(f"You: {msg}")
            self.entry.delete(0, tk.END)

    def display_message(self, msg):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, msg + "\n")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state='disabled')

# Run client GUI
if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()
