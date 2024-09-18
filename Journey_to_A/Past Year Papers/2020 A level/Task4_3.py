import flask, sqlite3
from Task4_2 import Person, Staff, Student

app = flask.Flask(__name__, template_folder = './TASK4_3_name_centre_index')

@app.route('/')

def home():
    with open(r'Computing-notes\Journey_to_A\Past Year Papers\2020 A level\people.txt') as f:
        data = []
        for line in f:
            line = line.strip().split(',')

            if line[2] == 'Person':
                p = Person(line[0], line[1])
                data += [(p.name, p.screen_name(), 'Person')]
            elif line[2] == 'Staff':
                p = Staff(line[0], line[1])
                data += [(p.name, p.screen_name(), 'Staff')]
            else:
                p = Student(line[0], line[1])
                data += [(p.name, p.screen_name(), 'Student')]


    return flask.render_template('home.html', data = data)

if __name__ == '__main__':
    app.run(debug = True)