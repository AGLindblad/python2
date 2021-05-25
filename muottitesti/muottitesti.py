from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/foo")
def foo():
  return render_template("foo.html")

app.run(debug=True)

