from app import app, db
from flask import render_template, Blueprint

#main = Blueprint('app', __name__)
#app = Flask(__name__)

#db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template(('index.html'))



# if __name__ == "__main__":
#     app.run(debug=True)