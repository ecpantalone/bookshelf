from flask import render_template, Blueprint
from app import app

#main = Blueprint('app', __name__)
#app = Flask(__name__)

#db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# if __name__ == "__main__":
#     app.run(debug=True)