import flask 
from flask import url_for 
 
app = flask.Flask(__name__) 
 
@app.route('/') 
def home(): 
  url1 = url_for('fixed_route') # live generation of URLs, can be fed into HTML templates for hyperlinks
  url2 = url_for('string_variable', s='example') 
  url3 = url_for('integer_variable', i=2020) 
  print(url1) 
  print(url2) 
  print(url3) 
  return 'Check your shell or command prompt window' 
 
@app.route('/fixed/') 
def fixed_route(): 
  return 'Routed to fixed()' 
 
@app.route('/string/<s>') 
def string_variable(s): 
  return f'Routed to string_variable(), s = {s}' 
 
@app.route('/integer/<int:i>') 
def integer_variable(i): 
  return f'Routed to integer_variable(), i = {i}' 
 
if __name__ == '__main__': 
  app.run()