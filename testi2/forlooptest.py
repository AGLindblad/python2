from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
  flowers = ["daffodil", "violet", "potato"]
  return render_template("base.html", flowers=flowers)

app.run(debug=True)

