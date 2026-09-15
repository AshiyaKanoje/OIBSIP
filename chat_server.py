import socket
import threading

host = "127.0.0.1"
port = 5000

server = socket.socket()
server.bind((host, port))
server.listen(2)

print("Chat server started")
print("Waiting for users...")

users = []


def chat(client, name):
    while True:
        try:
            msg = client.recv(1024).decode()

            if msg == "exit":
                print(name, "left the chat")
                break

            # send the message to the other user
            for user in users:
                if user != client:
                    user.send((name + ": " + msg).encode())

        except:
            break

    if client in users:
        users.remove(client)

    client.close()


while len(users) < 2:
    client, address = server.accept()

    client.send("Enter your name: ".encode())
    name = client.recv(1024).decode()

    users.append(client)

    print(name, "joined the chat")

    thread = threading.Thread(target=chat, args=(client, name))
    thread.start()

print("Both users are connected")
