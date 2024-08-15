import socket

# Create passive listening socket
listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 6789))
listen_socket.listen()

chat_socket , addr = listen_socket.accept()
while True:
    data = input('INPUT SERVER: ').encode()
    chat_socket.sendall(data + b'\n')
    if 'end connection'.encode() in data:
        break
    print('WAITING FOR CLIENT...')
    data = b''
    while b'\n' not in data:
        data += chat_socket.recv(1024)
    print(f'CLIENT WROTE: {data.decode()}')

    if 'end connection'.encode() in data:
        break

listen_socket.close()
