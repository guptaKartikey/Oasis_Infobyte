import socket
import threading

# Function to handle receiving messages from client
def receive_messages(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(f"\nClient: {msg}\nYou: ", end="")
        except:
            print("\nConnection closed by client.")
            break

def start_server():
    host = "127.0.0.1"   # Localhost (same machine)
    port = 12345         # Free port

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server started on {host}:{port}, waiting for connection...")
    conn, addr = server_socket.accept()
    print(f"Connected with {addr}")

    # Start receiving thread
    threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()

    # Sending messages
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            conn.send("Server has left the chat.".encode())
            break
        conn.send(msg.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
