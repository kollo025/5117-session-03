from flask import Flask, request, render_template # import Flask class and other
# from flask import *,

app = Flask(__name__) # create instance of Flask class (represents the server)

@app.route("/") # python annotation: tell Flask what url should trigger this function
def hello_world():
    return "<p>Hello, World!</p>"

# app.route is a function that returns a function


@app.route('/hi', methods=['GET']) # get method only route
def hi():
  user_name = request.args.get("userName", "unknown") # get username from query parameter
  return render_template('main.html', user=user_name) 

@app.route('/guestbook', methods=['GET']) # get method only route
def guestbook():
  return render_template('guestbook.html') 