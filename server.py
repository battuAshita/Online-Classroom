from flask import Flask, request, render_template
from pymongo import MongoClient
import urllib

app = Flask(__name__)

CONNECTION_STRING = "mongodb+srv://FlipR:" + urllib.parse.quote_plus(
    "Flipr@123") + "@flipr.ipovt.mongodb.net/flipr?retryWrites=true&w=majority"

# Create a connection using MongoClient
client = MongoClient(CONNECTION_STRING)

# Create a database named user data
db = client['flipr']


class User:

    def register(self, username, password, email, courses=None, loginType):
        if courses is None:
            courses = list()
        user = {
            "username": username,
            "password": password,
            "email": email,
            "courses_taken": courses
            "login_type":loginType
        }
        return user


@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "GET":
        return render_template("homePage.html")

    u = request.form['user']
    p = request.form['pass']

    # logging in to dashboard
    user_data = db.users.find_one({"username": u, "password": p}, {"username": 1, "courses_taken": 1, "_id": 0})

    if user_data['username'] != "":
        l = user_data['courses_taken']
        return render_template("dashboard.html", response=user_data, l=l)
    else:
        return render_template("error.html")


@app.route("/register", methods=["GET", "POST"])
def register_page():
    if request.method == "GET":
        return render_template("registerPage.html")

    u = request.form['username']
    p = request.form['password']
    e = request.form['email']
    c = request.form['courses_taken'].split(',')

    # Insert new user data to the database
    if u != "" and e != "":
        user = User().register(u, p, e, c)
        db.users.insert_one(user)

    return render_template("homePage.html")


@app.route("/dashboard", methods=["GET"])
def dashboard_page():
    if request.method == "GET":
        print('Dashboard')
        return render_template("dashboard.html")


@app.route("/assignments", methods=["GET", "POST"])
def assignments_page():
    if request.method == "GET":
        return render_template("Assignments.html")


@app.route("/tests", methods=["GET", "POST"])
def tests_page():
    if request.method == "GET":
        return render_template("tests.html")


@app.route("/calendar", methods=["GET", "POST"])
def calendar_page():
    if request.method == "GET":
        return render_template("calendar.html")


@app.route("/error", methods=["GET", "POST"])
def error_page():
    if request.method == "GET":
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
