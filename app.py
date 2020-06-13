# import library
from flask import Flask, render_template

aplikasi = Flask(__name__)

# Routes
from user import routes

@aplikasi.route("/")
def home():
    return render_template('home.html')

@aplikasi.route("/dashboard/")
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    aplikasi.run(debug=True, port=5005)
