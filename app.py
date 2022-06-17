"""Flask app for adopt app."""

from flask import Flask, request, redirect, render_template, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
# db.drop_all()
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_pets():
    """Shows pets on homepage"""

    pets = Pet.query.all()

    return render_template("homepage.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Displays pet add form; handle adding pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name,
        species=species,
        photo_url=photo_url,
        age=age,
        notes=notes)

        db.session.add(pet)
        db.session.commit()
        flash(f"Added {name} the {species} ")

        return redirect('/')

    else:
        return render_template('pet-add-form.html', form=form)


@app.route("/<int:pet_id_number>", methods=["GET", "POST"])
def edit_pet(pet_id_number):
    """Displays edit pet form; handle edit pet form"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data