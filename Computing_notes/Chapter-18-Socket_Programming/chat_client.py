import socket

chat_socket = socket.socket()
address = input('Enter the IP address of the server: ')
port = int(input('Enter the port number of the server: '))

chat_socket.connect((address, port))
while True:
    print('WAITING FOR SERVER')
    data = b''

    while b'\n' not in data:
        data += chat_socket.recv(1024)

    if 'end connection'.encode() in data:
        break

    print(f'SERVER WROTE: {data.decode()}')
    data = input('INPUT CLIENT: ').encode()
    chat_socket.sendall(data + b'\n')
    if 'end connection'.encode() in data:
        break

chat_socket.close()
    
