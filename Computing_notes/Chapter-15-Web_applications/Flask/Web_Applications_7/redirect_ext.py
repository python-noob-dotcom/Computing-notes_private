import flask 
from flask import redirect 
 
app = flask.Flask(__name__) 
 
@app.route('/') 
def index(): 
  return redirect('http://example.com') 
 
if __name__ == '__main__': 
  app.run() 