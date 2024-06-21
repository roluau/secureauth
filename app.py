from flask import Flask, render_template, request, jsonify
import pyotp
import json

app = Flask(__name__)

# Load existing TOTPs from JSON file
def load_totps():
    try:
        with open('totps.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

totps = load_totps()

@app.route('/')
def index():
    return render_template('index.html', totps=totps)

@app.route('/add_totp', methods=['POST'])
def add_totp():
    data = request.get_json()
    secret = data['secret']
    account = data['account']
    if not secret or not account:
        return jsonify({'error': 'Secret key and account name cannot be empty!'}), 400
    totps[account] = secret
    save_totps()
    return jsonify({'success': 'TOTP added successfully'}), 200

def save_totps():
    with open('totps.json', 'w') as f:
        json.dump(totps, f)

if __name__ == '__main__':
    app.run(debug=True)
