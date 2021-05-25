from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  infos = ["for-loop", "jinja", "html-form", "flask", "templates"]
  return render_template("base.html", infos=infos)

app.run(debug=True)

