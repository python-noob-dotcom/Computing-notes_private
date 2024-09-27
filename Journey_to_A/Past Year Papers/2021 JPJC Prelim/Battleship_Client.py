#Client socket
#============

def initGrid():
    global grid
    grid = [[0 for i in range(5)] for j in range(4)]
    global ship_loc
    ship_loc = 0

    return grid

def displayGrid():
    global grid
    for line in grid:
        for char in line:
            print(char, end='')
        print('')

def CheckRes(row, col):
    global ship_loc, grid

    if row == ship_loc[0] and col == ship_loc[1]:
        grid[row][col] = 'S'
        return True
    
    else:
        grid[row][col] = 'X'
        return False

import socket

client_socket = socket.socket()

address = input('Enter IPv4 address of server: ')
port = int(input('Enter port number of server: '))

client_socket.connect((address, port))

print('Welcome to Battleship!')

while True:
    ship_loc = client_socket.recv(1024).decode().strip().split(',')
    data = client_socket.recv(1024) #receive data from server
    
    
    if b"Enter" in data: #instruction received
        choice = input(data.decode()+ ': ') #get player to input number
        client_socket.sendall(choice.encode()) #send number to server
        choice = choice.split(',')

        CheckRes(int(choice[0]), int(choice[1]))
        displayGrid()
    
    else:
        print(data.decode()) #non-instruction received
        if b"GAME OVER" in data \
        or b"YOU WON" in data:
            break

client_socket.close()

