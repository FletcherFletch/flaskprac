from  flask import Flask

# create and initialize a new Flask app

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hellow. World!"

if __name__ == "__main__":
    app.run()