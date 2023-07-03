from main import app, db
from models import Attraction
from flask import request, jsonify



@app.route('/attractions', methods=['POST'])
def create_attraction():

    data = request.get_json()
    # create a new Attraction object
    new_attraction = Attraction(
        name=data['name'], 
        location=data['location'], 
        latitude=data.get('latitude'), 
        longitude=data.get('longitude'),
        description=data['description'], 
        opening_hours=data.get('opening_hours'), 
        entry_fees=data.get('entry_fees'), 
        website=data.get('website'), 
        contact_info=data.get('contact_info')
    )
    try:
        db.session.add(new_attraction)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise 

    return jsonify({'message': 'attraction successfully created '}), 201 



@app.route('/attractions',methods=['GET'])
def get_attractions():
    return "HELLO"