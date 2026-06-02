# Generated from: app.ipynb
# Converted at: 2026-06-02T17:26:51.607Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

from flask import Flask, jsonify
import random

app = Flask(__name__)

latest_data = {
    "temperature": 25,
    "occupancy": 0,
    "power": 200
}

@app.route('/data')
def get_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(debug=True)