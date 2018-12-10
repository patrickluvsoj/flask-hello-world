from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hi, there!"

@app.route("/search/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

@app.route("/name/<name>")
def name(name):
    if name.lower() == "patrick":
        return "Hello, " + name, 200
    else:
        return "Not Found", 404


if __name__ == "__main__":
    app.run()