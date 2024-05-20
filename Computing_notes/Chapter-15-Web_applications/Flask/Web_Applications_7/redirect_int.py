import flask 
from flask import redirect, url_for 
 
app = flask.Flask(__name__) 
 
@app.route('/new_url/') 
def moved_index(): 
  return 'You have reached the new URL!' 
 
@app.route('/') 
def index(): 
  return redirect(url_for('moved_index')) 
 
if __name__ == '__main__': 
  app.run() 