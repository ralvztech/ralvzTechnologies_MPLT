#!/usr/bin/python3
"""Starts a Flask Web Application"""
from flask import Flask, render_template
app = Flask(__name__, template_folder='template')


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/location")
def location():
    return render_template('location.html')


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)