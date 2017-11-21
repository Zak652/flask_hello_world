from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return render_template("hello_world.html", 
                            hello_world = "Hello World!")

@app.route("/<first>")
def hi_person(first):
	return render_template("hello_world.html", 
                            hello = "Hello", 
                            first = "{}".format(first.title()))

@app.route("/<first>")
def hello_person(first):
    return render_template("hello_world.html", 
                            hello = "Hello", 
                            first = "{}".format(first.title()), 
                            picture = "Here's a picture of a kitten. Awww...")

@app.route("/<first>/<last>")
def hello_jedi(first, last):
    return render_template("hello_world.html", 
                            hello = "Hello", 
                            first = "{}".format(first[1:]), 
                            last = "{}".format(last[0:3]))

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 8080)