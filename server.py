from flask import Flask, request, render_template
from pymongo import MongoClient
import urllib

app = Flask(__name__)


def get_database():
    CONNECTION_STRING = "data models+srv://FlipR:" + urllib.parse.quote_plus(
        "Flipr@123") + "@flipr.ipovt.data models.net/flipr?retryWrites=true&w=majority"

    # Create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create a database named user data
    return client['flipr']


@app.route("/home", methods=["GET", "POST"])
def home_page():
    if request.method == "GET":
        return render_template("homePage.html")


@app.route("/register", methods=["GET", "POST"])
def register_page():
    if request.method == "GET":
        return render_template("registerPage.html")


@app.route("/dashboard", methods=["GET"])
def dashboard_page():
    if request.method == "GET":
        print('Dashboard')
        return render_template("dashboard.html")


@app.route("/Assignments", methods=["GET", "POST"])
def assignments_page():
    if request.method == "GET":
        return render_template("Assignments.html")


@app.route("/Tests", methods=["GET", "POST"])
def tests_page():
    if request.method == "GET":
        return render_template("tests.html")


@app.route("/Calender", methods=["GET", "POST"])
def calender_page():
    if request.method == "GET":
        return render_template("calender.html")


if __name__ == "__main__":
    # Get the database
    db = get_database()
    # Dummy document
    user = {"first_name": "a"}

    db.users.insert_one(user)

    app.run(debug=True)
