from flask import Flask, render_template, redirect, request
from utils import init, view_expense, submit_expense, group_by_name, group_by_title

app = Flask(__name__)

init()


@app.route("/", methods=['GET'])
def home():
    return redirect("/create")


@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template("create.html")

    name = request.form["name"]
    title = request.form["title"]
    expense = request.form["expense"]
    date = request.form["date"]

    submit_expense(name, title, expense, date)

    return redirect("/expenses")


@app.route("/expenses", methods=["GET"])
def expenses():
    all_expenses, total = view_expense()
    expenses_by_user = group_by_name()
    expenses_by_title = group_by_title()

    return render_template("expenses.html", expenses=all_expenses, total=total, by_user=expenses_by_user,
                           by_title=expenses_by_title)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect("/create")
    return render_template("login.html")


app.run(debug=True)
