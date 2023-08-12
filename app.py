from flask import Flask

app = Flask(__name__)

@app.route("/h")
def hello_world():
    return "Hello, World access it!"

@app.route("/h1")
def hello_world1():
    return "Hello, World 1!"

@app.route("/h2")
def hello_world2():
    return "Hello, World 2"

if __name__=="__main__":
    app.run(host="0.0.0.0")
