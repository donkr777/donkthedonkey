# app.py
from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def home():
    return render_template('index.html')

# This is required for Frozen-Flask to know what to freeze
@freezer.register_generator
def home():
    yield '/'

if __name__ == '__main__':
    freezer.freeze()  # Use this to build static files
    # app.run(debug=True)  # Uncomment for local testing