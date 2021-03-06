from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields.datetime import DateField
from wtforms.fields import DecimalField


class AddRadrennenForm(FlaskForm):
    RadrennenID = StringField("RadrennenID")
    Titel = StringField("Titel")
    Land = StringField("Land")
    Datum = DateField("Datum")
    LaengeInKm = DecimalField("Länge in Km")
