from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load data from JSON file
with open('data/jsondata.json') as f:
    data = json.load(f)

# Endpoint to serve the dashboard page
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# API route to provide data for frontend
@app.route('/api/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
