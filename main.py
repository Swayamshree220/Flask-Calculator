from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/input")
def input_page():
    return render_template("input.html", title="Calculator")

@app.route("/calc/<int:num1>/<int:num2>/<operation>")
def calc(num1, num2, operation):
    if operation == "add":
        output = num1 + num2
    elif operation == "sub":
        output = num1 - num2
    elif operation == "mul":
        output = num1 * num2
    elif operation == "div":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        output = num1 / num2
    else:
        return "Invalid operation"
    return f"<h1>Result: {num1} {operation} {num2} = {output}</h1>"

@app.route("/check/<int:num1>/<int:num2>/<operation>")
def check(num1, num2, operation):
    if operation not in ["add", "sub", "mul", "div"]:
        return redirect(url_for("home"))
    return redirect(url_for("calc", num1=num1, num2=num2, operation=operation))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
