from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField


class AddHauptsponsorForm(FlaskForm):
    SponsorID = StringField("SponsorID")
    Name = StringField("Name")
    Sponsorbetrag = DecimalField("Sponsorbetrag")
    Werbungsart = StringField("Land")
    Land = StringField("Radmarke")
