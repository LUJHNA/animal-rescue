from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, NumberRange, URL, Email

class AnimalForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=64)])
    species = StringField('Species', validators=[DataRequired(), Length(max=64)])
    breed = StringField('Breed', validators=[Optional(), Length(max=64)])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    gender = SelectField('Gender', choices=[('', 'Select Gender'), ('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown')])
    description = TextAreaField('Description', validators=[Optional()])
    image_url = StringField('Image URL', validators=[Optional(), URL(), Length(max=256)])
    status = SelectField('Status', choices=[('Available', 'Available'), ('Pending', 'Pending'), ('Adopted', 'Adopted')], default='Available')
    submit = SubmitField('Submit')

class AdopterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=64)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(max=20)])
    address = TextAreaField('Address', validators=[Optional(), Length(max=256)])
    submit = SubmitField('Submit Adoption Application')