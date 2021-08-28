from flask import Flask
from pymongo import MongoClient
import urllib

app = Flask(__name__)


def get_database():
    CONNECTION_STRING = "mongodb+srv://FlipR:" + urllib.parse.quote_plus(
        "Flipr@123") + "@flipr.ipovt.mongodb.net/flipr?retryWrites=true&w=majority"

    # Create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create a database named user data
    return client['flipr']


@app.route("/home", methods=["GET"])
def home_page():
    print('Welcome to the home page')


@app.route("/dashboard", methods=["GET"])
def dashboard():
    print('Dashboard')


if __name__ == "__main__":
    # Get the database
    db = get_database()
    # Dummy document
    user = {"first_name": "a"}

    db.users.insert_one(user)

    app.run(debug=True)
