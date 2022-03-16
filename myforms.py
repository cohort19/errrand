from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField

from wtforms.validators import DataRequired, Email, Length



#d main syntax is variable = FieldType('label',validator=[])    