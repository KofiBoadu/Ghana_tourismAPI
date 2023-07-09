from models import Attraction
from flask import request, jsonify
from database import db

def initialize_routes(app):

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
        try:
            all_attractions= Attraction.query.all()
            list_ofAttractions=[ attractions.convert_to_dict() for attractions in all_attractions]
            return jsonify(list_ofAttractions),200

        except Exception as e :
            return jsonify({"error": str(e)}), 500






    @app.route('/attractions/<attraction_id>', methods=['DELETE'])
    def delete_attraction(attraction_id):
        attraction = Attraction.query.get(attraction_id)
        if attraction:
            # Delete the attraction from the database
            name= attraction.name
            db.session.delete(attraction)
            db.session.commit()
            return jsonify({'message': f'Attraction {name} deleted successfully'}), 200

        else:

            return jsonify({'error': 'Attraction not found'}), 404





    
    @app.route('/attractions', methods=['DELETE'])
    def delete_all_attractions():
        # Get the names of all attractions before deleting them
        all_attractions = Attraction.query.all()

        if len(all_attractions) == 0:
            return jsonify({'message': 'No attractions found to delete'}), 404

        try:
            # Delete all attractions from the database
            db.session.query(Attraction).delete()
            db.session.commit()

            # Return a JSON response with the names of the deleted attractions
            return jsonify({'message': 'All attractions deleted successfully'}), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({'error': f'Error occurred while deleting attractions: {str(e)}'}), 500

