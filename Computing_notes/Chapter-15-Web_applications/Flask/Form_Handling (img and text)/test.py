import flask, os, sqlite3 
from flask import render_template, request 
from flask import send_from_directory 
from werkzeug.utils import secure_filename 
 
if not os.path.isfile('db.sqlite3'): 
  db = sqlite3.connect('db.sqlite3') 
  db.execute('CREATE TABLE photos(photo TEXT)') 
  db.commit() 
  db.close() 
     
app = flask.Flask(__name__) 
 
@app.route('/', methods=['GET', 'POST']) 
def landing(): 
  if request.method == 'POST' and request.files and 'photo' in request.files: 
    # Save file 
    photo = request.files['photo'] 
    filename = secure_filename(photo.filename)
    print(filename)
    path = os.path.join('uploads', filename) 
    photo.save(path) 
    # Add filename to database 
    db = sqlite3.connect('db.sqlite3') 
    db.execute('INSERT INTO photos(photo) VALUES(?)', 
               (filename,)) 
    db.commit() 
    db.close() 
  return render_template('form_with_file_upload.html') 
 
@app.route('/view', methods = ['GET', 'POST']) 
def view(): 
  db = sqlite3.connect('db.sqlite3') 
  cur = db.execute('SELECT photo FROM photos') 
  photos = [] 
  for row in cur: 
    photos.append(row[0]) 
  db.close() 
  return render_template('view_file_uploads.html', 
                         photos=photos) 
 
@app.route('/photos/<filename>') 
def get_file(filename): 
  return send_from_directory('uploads', filename) 
 
if __name__ == '__main__': 
  app.run()
