from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique = True, nullable = False)
	img_url = db.Column(db.String(20), nullable=False, default="default.jpg")
	password_hash = db.Column(db.String(128), nullable=False)
	communities = db.relationship("Community", backref="user")

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
	 	return check_password_hash(self.password_hash, password)

	def __repr(self):
		return f"User({self.username})','{self.email}','{self.img_url}','{self.password}"

class Community(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	address = db.Column(db.String(255), nullable=False)
	name = db.Column(db.String(30), nullable=False, default=f"Community {id}")
	pi_zero_ip_address = db.Column(db.String(40), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	plants = db.relationship("Plant", backref="community")

	def __repr(self):
		return f"Community({self.name}','{self.pi_zero_ip_address})"

# class WeatherData(db.Model):
	#Define a one to one relationship with the commmunity table because a community
	#should have many data entry points for the weather for the predition algo to work on it


class Plant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	img_url = db.Column(db.String(20), nullable=False)
	community_id = db.Column(db.Integer, db.ForeignKey("community.id"))


	def __repr__(self):
		return f"Plant({self.name}','{self.img_url})"




