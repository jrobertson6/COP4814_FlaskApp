
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Optional
from flask_wtf.file import FileField, FileAllowed

class PhoneForm(FlaskForm):
    phone_number = StringField("Enter a phone number", validators=[Optional()])
    country_code = SelectField("Select Country Code", choices=[
        ("+1", "United States (+1)"),
        ("+44", "United Kingdom (+44)"),
        ("+91", "India (+91)"),
        ("+61", "Australia (+61)"),
        ("+81", "Japan (+81)"),
        ("+49", "Germany (+49)"),
        ("+33", "France (+33)"),
        ("+39", "Italy (+39)"),
        ("+55", "Brazil (+55)"),
        ("+27", "South Africa (+27)")
    ])
    csv_file = FileField("Or upload a CSV file", validators=[FileAllowed(['csv'], 'CSV files only!')])
    submit = SubmitField("Verify")
