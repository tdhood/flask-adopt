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


<form id="pet-add-form" method="POST">
    {{ form.hidden_tag() }}

    {% for field in form
        if field.widget.input_type != 'hidden' %}
    
    <p>
    {{ field.label }}
    {{ field }} 

    {% for error in field.errors %}
        {{ error }}
    {% endfor %}
    </p>

    {% endfor %}

    <button type="submit">Add</button>
</form>