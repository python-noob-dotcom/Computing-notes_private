import socket, random

# game code
def initGrid():
    global grid
    grid = [[0 for i in range(5)] for j in range(4)]
    global ship_loc
    ship_loc = [random.randint(0, 3), random.randint(0, 4)]

    return grid

def validateRow(row):
    if row < 0 or row > 4:
        return False
    else:
        return True
    
def validateColumn(col):
    if  col < 0 or col > 5:
        return False
    else:
        return True
    
def CheckRes(row, col):
    global ship_loc, grid

    if row == ship_loc[0] and col == ship_loc[1]:
        grid[row][col] = 'S'
        return True
    
    else:
        grid[row][col] = 'X'
        return False
    
initGrid()

my_sock = socket.socket()

my_sock.bind(('127.0.0.1', 6789))

my_sock.listen()

conn, addr = my_sock.accept()

game_end = False

while not game_end:
    conn.sendall(ship_loc[0].encode() + b',' + ship_loc[1].encode() + b'\n')
    conn.sendall(b'Enter\n')

    row_col = b''

    while b'\n' not in row_col:
        row_col += conn.recv(1024)

    row, col = row_col.decode().strip().split(',')

    if validateColumn(int(col)) and validateRow(int(row)):
        game_end = CheckRes(int(row), int(col))
        displayGrid(grid)

        if game_end:
            conn.sendall(b'GAME OVER\n')
        else:
            conn.sendall(b'Continue\n')

