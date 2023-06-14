from flask import Flask, render_template, request, redirect
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from PIL import Image

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form['name']
        breed = request.form['breed']
        age = int(request.form['age'])
        weight = float(request.form['weight'])

        # Store the pet's information in a database or file
        # (you can use SQLite, JSON, or any other suitable option)

        return redirect('/')

    return render_template('profile.html')


if __name__ == '__main__':
    app.run()
