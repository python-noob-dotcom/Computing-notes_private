import flask, os, sqlite3
from flask import render_template, request, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename # prevents using special filename to hack the database

# if not os.path.isfile('photos_2.db'):
with sqlite3.connect('photos.db') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS "photos"\
                   ("photo" TEXT)')
    conn.commit()

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def landing():
    if request.method == 'POST' and \
        request.files and 'photo' in request.files:
        # Save File
        photo = request.files['photo']
        filenames = secure_filename(photo.filename) 
        # remove stuff like double dots that access parent directory
        path = os.path.join('uploads', filenames)
        photo.save(path)
        
        with sqlite3.connect('./photos.db') as conn:
            cursor = conn.cursor()

            cursor.execute('BEGIN TRANSACTION')

            cursor.execute('INSERT INTO photos(photo) VALUES(?)', 
                           (filenames,))

            conn.commit()
                

    return render_template('form_with_file_upload.html')

@app.route('/view', methods = ['GET', 'POST'])

def view():
    with sqlite3.connect('./photos.db') as conn:
        cursor = conn.cursor()
        photos = []
        res = cursor.execute('SELECT photo FROM photos')
        for row in res:
            photos += [row[0]]
        
    return render_template('view_file_uploads.html', photos = photos)

@app.route('/photos/<filename>')

def get_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run(debug = True)
