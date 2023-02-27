import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    # return flask.render_template("index.html")
    return 'please press the like btn!!!'

@app.route('/home')
def aaa():
    return flask.render_template("aaa.html", a=70, b=30)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')