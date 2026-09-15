import socket
import threading
from datetime import datetime

host = "127.0.0.1"
port = 5000

client = socket.socket()
client.connect((host, port))

name_message = client.recv(1024).decode()
name = input(name_message)

client.send(name.encode())

print("You are connected to the chat")
print("Type exit to leave")


def receive_message():
    while True:
        try:
            message = client.recv(1024).decode()

            if message:
                time = datetime.now().strftime("%H:%M")
                print("\n[" + time + "] " + message)
                print("You: ", end="")

        except:
            break


thread = threading.Thread(target=receive_message)
thread.daemon = True
thread.start()


while True:
    message = input("You: ")

    client.send(message.encode())

    if message.lower() == "exit":
        break

client.close()