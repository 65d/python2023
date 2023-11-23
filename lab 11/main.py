import tkinter as tk
from tkinter import scrolledtext, StringVar
import socket
import threading

class UsernameEntryWindow:
    def __init__(self, master, chat_client):

        self.master = master
        self.master.title("Enter Username")

        self.label = tk.Label(self.master, text="Enter Your Username:")
        self.label.pack(pady=10)
        self.master.geometry("300x200")

        # Make the window non-resizable
        self.master.resizable(False, False)
        self.username_entry = tk.Entry(self.master, width=20)
        self.username_entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_username)
        self.submit_button.pack(pady=10)

        self.chat_client = chat_client

    def submit_username(self):
        username = self.username_entry.get()
        if username:
            self.chat_client.set_username(username)
            self.master.destroy()

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Chat")

        self.username = ""
        self.room_id = ""

        self.message_entry = tk.Entry(self.master, width=50)
        self.message_entry.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

        self.send_button = tk.Button(self.master, text="Send", command=self.send_message)
        self.send_button.grid(row=2, column=3, padx=10, pady=10)

        self.room_id_entry = tk.Entry(self.master, width=20)
        self.room_id_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.chat_box = scrolledtext.ScrolledText(self.master, width=60, height=20, wrap=tk.WORD, state=tk.DISABLED)
        self.chat_box.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))

        self.username = "Your Username"

        self.master.geometry("550x500")

        self.master.resizable(False, False)

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        self.username_window = tk.Toplevel(self.master)
        self.username_entry_window = UsernameEntryWindow(self.username_window, self)

    def set_username(self, username):
        self.username = username

    def send_message(self):
        message = self.message_entry.get()
        room_id = self.room_id_entry.get()
        if self.username and message and room_id:
            full_message = f"[Room {room_id}] {self.username}: {message}"
            self.client_socket.send(full_message.encode())
            self.display_message(full_message)  # Display the sent message in the chat box
            self.message_entry.delete(0, 'end')

    def receive_messages(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            if not message:
                break
            self.display_message(message)

    def display_message(self, message):
        # Extract room_id from the message
        room_id_index = message.find("[Room")
        if room_id_index != -1:
            room_id = message[room_id_index + 6: message.find("]", room_id_index)]
            if room_id == self.room_id_entry.get():
                self.chat_box.config(state=tk.NORMAL)
                self.chat_box.insert('end', f"{message}\n", 'blue')
                self.chat_box.yview(tk.END)
                self.chat_box.config(state=tk.DISABLED)



if __name__ == "__main__":
    root = tk.Tk()
    client_app = ChatClient(root)
    client_app.chat_box.tag_config('blue', foreground='blue')
    root.mainloop()
