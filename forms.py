"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, IntergerField

class AddPetForm(FlaskForm):
    """form for adding pets"""

    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo")
    age = IntergerField("Age")
    notes = StringField("Notes")


<form id