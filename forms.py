from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DNAForm(FlaskForm):
    dna = StringField('DNA:', validators=[DataRequired()])
    submit = SubmitField('Convert')