def decrypt(msg):
    dec = ''

    j = len(msg)

    for char in msg:
        if ord(char) == 32:
            num = 127 - j
        else:
            num = ord(char) - j

        dec += chr(num)
        j -= 1

    return dec
    
	
#main program
import socket, csv, datetime
#type your server code here

my_sock = socket.socket()

my_sock.bind(('127.0.0.1', 12345))

print("-"*20)
print("SERVER OPEN")
print("-"*20)

with open('LOG.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['Date/Time', 'clinet ip address', 'client port number',
                     'encrypted message', 'decrypted message'])

my_sock.listen()

conn, addr = my_sock.accept()

while True:
    data = b''

    while b'\n' not in data:
        data += conn.recv(1024)

    data = data.strip(b'\n')

    print(f'Encrypted message: {data.decode()}')
    print(f'Decrypted message: {decrypt(data.decode())}')

    with open('LOG.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow([datetime.datetime.now(), conn, addr, data.decode(), decrypt(data.decode())])

    status = input('Do you want to continue listening? [Y/N]: ')

    if status == 'N':
        conn.sendall(b'N\n')
        break
    else:
        conn.sendall(b'Y\n')
        continue

my_sock.close()
