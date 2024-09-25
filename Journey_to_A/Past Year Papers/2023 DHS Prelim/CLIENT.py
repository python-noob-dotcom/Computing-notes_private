def encrypt(plaintext):
    msg = ''
    j = len(plaintext)
    for i in range(len(plaintext)):
        num = ord(plaintext[i]) + j
        if num > 126:
            num = 32

        msg += chr(num)
        j -= 1

    return msg
	

#main program
import socket

print("-------------------")
print("CLIENT OPEN")
print("-------------------")
print()

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 9999))

while True:
    message = input("Enter message: ")
    encrypted_message = encrypt(message)

    data = encrypted_message.encode()
    my_socket.sendall(data + b'\n')
    print("message sent")
    print("-------------------")

    data = b''

    while b'\n' not in data:
        data += my_socket.recv(1024)
    
    data = data.strip(b'\n')

    if data.decode() == 'N':
        break
    else:
        continue

my_socket.close()

print("-------------------")
print("CLIENT CLOSED")
print("-------------------")
