import socket

my_socket = socket.socket()
my_socket.bind(('127.0.0.1', 12345)) # this is a tuple consisting of the IP address string and the port number

my_socket.listen() # after binding, start listening so that you can take in connections

new_socket, addr = my_socket.accept()
print(f'Connected to {str(addr)}')


print(new_socket.recv(1024))# b'' is converting string to raw bytes

new_socket.close()
my_socket.close()
