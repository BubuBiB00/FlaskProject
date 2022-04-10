from MySQLdb import Date
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields.datetime import DateField
from wtforms.fields import DecimalField


class Add_radrennen_form(FlaskForm):
    Titel = StringField("Titel")
    Land = StringField("Land")
    Datum = DateField("Datum")
    LaengeInKM = DecimalField("Länge in Km")
