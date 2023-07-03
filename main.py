from flask import Flask 
from flask_sqlalchemy import SQLAlchemy



app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attractions.db'
db= SQLAlchemy(app)


def initialize_routes():
    from routes import create_attraction, get_attractions
    app.add_url_rule('/attractions', view_func=create_attraction, methods=['POST'])
    app.add_url_rule('/attractions', view_func=get_attractions, methods=['GET'])



if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # create the database tables
    initialize_routes()
    app.run(debug=True)