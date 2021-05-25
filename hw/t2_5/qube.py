from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  cubic = 0
  if "side" in request.form:
    side = int(request.form["side"])
    cubic = side*side*side
  return render_template("index.html", cubic=cubic)

app.run(debug=True)
