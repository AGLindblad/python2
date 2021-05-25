from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"] )
def index():
  return render_template("index.html")

@app.route("/foo")
def foo():
  return render_template("foo.html")

app.run(debug=True)
