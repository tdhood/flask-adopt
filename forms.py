"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Optional, URL, AnyOf


class AddPetForm(FlaskForm):
    """form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(),
                                                 AnyOf(values=['cat', 'dog', 'porcupine'])])
    photo_url = StringField("Photo", validators=[Optional(), URL()])
    age = StringField("Age", validators=[InputRequired(),
                                          AnyOf(values=['baby', 'young', 'adult', 'senior'])])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """for for editing a pet"""

    photo_url = StringField("Photo", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Available", validators=[InputRequired()])