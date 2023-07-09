
from flask import Flask 
from database import db
from routes import initialize_routes

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attractions.db'
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # create the database tables
    initialize_routes(app)
    app.run(debug=True)







