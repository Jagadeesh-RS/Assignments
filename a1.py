from flask import Flask
app = Flask(__name__)
@app.route("/abc")
def abc():
    return "abc111"

@app.route('/put')
def ww():
    dat=request.args.get('x')
    return "This is the given value = {}".format(dat)

if __name__ == ("__main__"):
    app.run(host="0.0.0.0")
