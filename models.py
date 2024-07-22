from car app import db, login_manager
from datetime import datetime
rom flask_login import UserMixin


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    token = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.email}>'
    


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# main/models.py
from car_inventory import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Car {self.make} {self.model} {self.year}>'


# main/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class CarForm(FlaskForm):
    make = StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    submit_button = SubmitField('Submit')
