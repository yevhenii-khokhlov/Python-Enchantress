from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'It is my flask simple app.'


@app.route('/info')
def info():
    return 'It is my flask simple app.'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
