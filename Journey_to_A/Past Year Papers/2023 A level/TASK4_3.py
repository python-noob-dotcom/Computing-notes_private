import flask

data = []
with open('decompressedimage.txt') as f:
    for row in f:
        data += [row.strip()]

new_data = []

for i in range(len(data), 3):
    if data[i : i+3] == '000':
        new_data += 'red'
    elif data[i : i + 3] == '001':
        new_data += 'white'
    elif data[i : i + 3] == '010':
        new_data += 'yellow'
    elif data[i : i + 3] == '011':
        new_data += 'blue'
    elif data[i : i + 3] == '100':
        new_data += 'black'
    elif data[i : i + 3] == '110':
        new_data += 'green'


app = flask.Flask(__name__)
@app.route('/')

def home():
    return flask.render_template(data = new_data)