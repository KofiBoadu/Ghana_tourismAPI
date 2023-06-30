from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attractions.db'
db= SQLAlchemy(app)






# @app.route('/attractions',methods=['POST'])
# def create_attraction():
#     data= request.get_json()

#     #create a new attraction object 
#     new_attraction= Attraction