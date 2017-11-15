from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
	return "Hello {}".format(name.title())

@app.route("/hey/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

@app.route("/jedi/<first>/<last>")
def hello_jedi(first, last):
	return "Hello {}{}".format(last[0:3], first[1:])

if __name__ == "__main__":
    app.run(host=environ.get('IP', '0.0.0.0'),
            port=int(environ.get('PORT', '8080')))