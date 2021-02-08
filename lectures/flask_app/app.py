from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<name>")
@app.route("/")
def hello(name=None):
    return render_template("world.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
