from flask import render_template
from app import app 
from models.order_list import orders
#below is a 'decorator'.
# @app.route('/')
# def index():
#     return "Hello, world!"

@app.route('/')
def index():
    return render_template("index.html", title="Sean and Sons")

@app.route("/orders")
def show_tasks():
    return render_template("index.html", big_seans_orders = orders)

@app.route("/orders/<num>")
def show_order(num):
    return render_template("order.html", order = orders[int(num)])

