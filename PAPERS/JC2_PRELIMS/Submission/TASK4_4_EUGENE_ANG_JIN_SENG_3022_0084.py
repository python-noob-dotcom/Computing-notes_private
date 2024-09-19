import flask

app = flask.Flask(__name__, template_folder = './TASK4_4_EUGENE_ANG_JIN_SENG_3022_0084')
# Task 4.1

def init():
    global grid

    grid = [['--' for i in range(3)] for i in range(3)]

    global tries
    tries = 0

    global mine_x
    global mine_y

# Task 4.2
import random

def mine_loc():
    global mine_x
    global mine_y
    
    mine_y = mine_x = random.randint(0, 2)

def userin():
    x, y = input('Enter the x and y coordinates between 0 and 2 in the format: x,y. ').split(',')
    
    while x not in '012' and y not in '012':
        x, y = input('Enter the x and y coordinates between 0 and 2 in the format: x,y. ').split(',')
    
    return int(x), int(y)
        
def movement(x, y):
    global mine_x
    global mine_y
    global grid
    global tries
    
    if x == mine_x and y == mine_y:
        grid[y][x] = 'X'
    else:
        grid[y][x] = 'O'
        
    tries += 1
    
# Task 4.3

def display(grid):
    for row in grid:
        print(f'{row}')
        
def game_end(grid):
    for row in grid:
        for item in row:
            if item == 'X':
                return True
            
    return False

def main():
    init()
    global tries
    mine_loc()
    
    while not game_end(grid):
        display(grid)
        x, y = userin()
        movement(x, y)
    display(grid)
    print(f'You took {tries} tries to get the mine')
	
# init game stuff
init()
mine_loc()

        
@app.route('/', methods = ["GET", "POST"])

def home():
	global tries, grid, mine_x, mine_y
	if game_end(grid):
            # since game ended, need to not show the form but display the grid also
		return flask.render_template('game_end.html', grid= grid, game_end = True, tries = tries)
	else:
		if flask.request.method == 'GET':
                    # first time accessing, just render with nothin except the grid and whatever shit
			return flask.render_template('game_end.html', grid= grid, game_end = False, tries = tries)
		else:
                    # not first time running, need to backend process the movement and then update the grid
			x = flask.request.form['x']
			y = flask.request.form['y']
			
			movement(int(x), int(y))
			return flask.render_template('game_end.html', grid= grid, game_end = game_end(grid), tries = tries)

if __name__ == '__main__':
	app.run(debug = True)
	

