import socket
import threading

class ChatServer:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', 12345))
        self.server.listen()

        self.clients = []

        accept_thread = threading.Thread(target=self.accept_clients)
        accept_thread.start()

    def accept_clients(self):
        while True:
            conn, addr = self.server.accept()
            self.clients.append(conn)

            client_thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            client_thread.start()

    def handle_client(self, conn, addr):
        while True:
            message = conn.recv(1024).decode()
            if not message:
                break

            for client in self.clients:
                if client != conn:
                    try:
                        client.send(message.encode())
                    except:
                        self.clients.remove(client)

if __name__ == "__main__":
    server = ChatServer()
