from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask! This is my first app."


@app.route('/about')
def about():
    return "This is the About page."


@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to Flask. jUst trying to see if it works."


if __name__ == '__main__':
    app.run(debug=True)
