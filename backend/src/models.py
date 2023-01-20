from .database import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True) # SQLAlchemy automatically auto increment
	username = db.Column(db.String(16), nullable=False, unique=True) 
	password = db.Column(db.String(16), nullable=False)
	email = db.Column(db.String(50), unique=True)
	phone = db.Column(db.String(16))
	address = db.Column(db.String(200))
	city = db.Column(db.String(16))
	country = db.Column(db.String(16))
	birthdate = db.Column(db.String(16))

class Event(db.Model): 
	id = db.Column(db.Integer, primary_key=True) # SQLAlchemy automatically auto increment
	user_id = db.Column(db.Integer, nullable=False, foreign_key=True)
	parent_id = db.Column(db.Integer)
	name = db.Column(db.String(50), nullable=False)
	start_time = db.Column(db.DateTime, nullable=False) 
	end_time = db.Column(db.DateTime, nullable=False)
	type = db.Column(db.String(20))
	location = db.Column(db.String(50)) 
	overview = db.Column(db.String(200)) 
	# participantsId = db.Column(db.ARRAY(db.Integer)) #list of known participants
	# participantsName = db.Column(db.ARRAY(db.String)) #list of unknown participants
