import flask

app = flask.Flask(__name__)


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function


@app.route("/")
def hello_world():
    return "<h1 style=text-align:center>Hello, World!</h1>" \
           "<p>This is a paragraph</p>" \
           "<img src=https://media.giphy.com/media/fnlXXGImVWB0RYWWQj/giphy.gif>"


@app.route("/bye")
@make_emphasis
@make_bold
@make_underline
def say_bye():
    return "Bye"


@app.route("/<path:name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
