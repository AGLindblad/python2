from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  lion = "bob"
  return render_template("base.html", bob=lion)

app.run(debug=True)

