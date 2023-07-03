from main import db 


class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    description = db.Column(db.Text, nullable=False)
    opening_hours = db.Column(db.String(50))
    entry_fees = db.Column(db.Float)
    website = db.Column(db.String(200))
    contact_info = db.Column(db.String(200))
    


    def convert_to_dict(self):

        return {
            "id":self.id,
            "name": self.name,
            "location":self.location,
            "latitude":self.latitude,
            "longitude":self.longitude,
            "description":self.description,
            "opening_hours":self.opening_hours,
            "entry_fees": self.entry_fees,
            "website": self.website,
            "contact_info": self.contact_info
        }