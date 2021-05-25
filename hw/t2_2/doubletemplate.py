from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/foobar")
def foobar():
  return render_template("foobar.html")

app.run(debug=True)

