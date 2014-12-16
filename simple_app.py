from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name="Treehouse"):
    #return "Hello from {}".format(name)
    context = {"name": name}
    return render_template("index.html", **context)

@app.route("/add/<int:num1>/<int:num2>")
@app.route("/add/<float:num1>/<float:num2>")
@app.route("/add/<int:num1>/<float:num2>")
@app.route("/add/<float:num1>/<int:num2>")
def add(num1, num2):
    #return "{} + {} = {}".format(num1, num2, num1+num2)
    #return """
    #<!DOCTYPE html>
    #<html>
    #    <head>
    #        <title>Adding:</title>
    #   </head>
    #    <body>
    #        <h1>{} + {} = {}</h1>
    #    </body>
    #</html>
    #""".format(num1, num2, num1+num2)
    context = {"num1": num1, "num2": num2}
    return render_template("add.html", **context)

app.run(debug=True)