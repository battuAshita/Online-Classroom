from flask import jsonify, request


def register():
    user = {
        "username": request.form['username'],
        "password": request.form['Password'],
        "email": request.form['email'],
        "courses_taken": request.form['courses']
    }
    return jsonify(user), 200
