#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


# 1️⃣ Index Route
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


# 2️⃣ Print String Route
@app.route("/print/<string:param>")
def print_string(param):
    print(param)  # prints to console
    return param  # displays in browser


# 3️⃣ Count Route
@app.route("/count/<int:param>")
def count(param):
    numbers = ""
    for i in range(param):
        numbers += f"{i}\n"
    return numbers


# 4️⃣ Math Route
@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2   # fix here
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)
