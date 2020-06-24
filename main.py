from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

db = SQLAlchemy(app)

# class User(db.Model):
#     email_address = db.Column(db.String(250), primary_key=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)