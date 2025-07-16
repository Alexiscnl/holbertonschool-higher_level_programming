#!/usr/bin/python3
from flask import Flask, render_template
import json
from flask import request
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
        return render_template('items.html', items=data['items'])
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return render_template('items.html', items=[])

@app.route('/products')
def products():
    source = request.args.get("source", "json")
    product_id = request.args.get("id")
    error_message = None

    if source not in ["json", "csv", "sql"]:
        error_message = "Wrong source"
        return render_template('product_display.html', error=error_message)

    if source == "json":
        with open("products.json") as f:
            data = json.load(f)

    if source == "csv":
        with open("products.csv", newline="") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

    if source == "sql":
        data = product_from_sqlite(product_id)
        if product_id and not data:
            error_message = "Product not found"
            return render_template("product_display.html", error=error_message)
        return render_template("product_display.html", products=data)

    if product_id:
        found = None
        for item in data:
            if int(product_id) == int(item["id"]):
                found = item
                break
        if found:
            data = [found]
        else:
            error_message = "Product not found"
            return render_template("product_display.html", error=error_message)

    return render_template("product_display.html", products=data)

def product_from_sqlite(id_param=None):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    if id_param:
        cursor.execute('SELECT id, name, category, price FROM Products WHERE id=?', (id_param,))
    else:
        cursor.execute('SELECT id, name, category, price FROM Products')

    rows = cursor.fetchall()
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    conn.close()
    return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)
