import socket

my_socket = socket.socket()

address = input('Enter IPv4 address of server: ')
port = int(input('Enter port number of server: '))

my_socket.connect((address, port))
my_socket.sendall(b'Hello from server\n') # b'' is converting string to raw bytesnew_socket.sendall(b'Hello from server\n') # b'' is converting string to raw bytes

my_socket.close()

    
