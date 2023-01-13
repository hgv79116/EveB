from .db import db
import sqlalchemy as sa


class User(db.Model):
	userId = sa.Column(sa.Integer, primary_key=True, nullable=False)
	userName = sa.Column(sa.String, nullable=False) 
	password = sa.Column(sa.String, nullable=False)
	email = sa.Column(sa.String)
	phoneNumber = sa.Column(sa.String)

class Event(db.Model): 
	eventId = sa.Column(sa.Integer, primary_key=True, nullable=False)
	userId = sa.Column(sa.Integer, nullable=False, foreign_key=True)
	parentId = sa.Column(sa.Integer)
	name = sa.Column(sa.String, nullable=False)
	startTime = sa.Column(sa.DateTime, nullable=False) 
	endTime = sa.Column(sa.DateTime, nullable=False)
	eventType = sa.Column(sa.String)
	location = sa.Column(sa.String) 
	overview = sa.Column(sa.String) 
	# participantsId = sa.Column(sa.ARRAY(sa.Integer)) #list of known participants
	# participantsName = sa.Column(sa.ARRAY(sa.String)) #list of unknown participants

	
class sth(): 
    pass