import flask, pymongo

app = flask.Flask(__name__, template_folder = 'TASK4_4')

@app.route('/')

def home():
    return flask.render_template('home.html')

@app.route('/res', methods = ['POST'])

def res():
    brand = flask.request.form['brand']

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    db = connection['jp_mobile']
    coll = db['phone']

    res = list(coll.find({'brand':brand}).sort('price'))

    return flask.render_template('res.html', data = res)

if __name__ == '__main__':
    app.run(debug = True)

