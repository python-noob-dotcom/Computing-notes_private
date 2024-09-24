import socket

def main():
    client_socket = socket.socket()
    client_socket.connect(("127.0.0.1", 12347))
    
    print("Connected to Chatterbot server.")
    
    while True:
        user_input = input("You: ")
        client_socket.send(user_input.encode()+b'\n')
        if user_input.lower() == "exit":
            break
        response = b""
        while b'\n' not in response:
            response += client_socket.recv(1024)
        response = response.decode()
        print("Chatterbot:", response)
    
    print("Goodbye! Connection closed.")
    client_socket.close()

main()
