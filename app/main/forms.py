from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,
from wtforms.validators import Required

class Pitchform(FlaskForm):
    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('1', 'Investor Pitch'), ('2', 'Pick-up Lines'), ('3', 'product pitch')])
    submit = SubmitField('Submit')
    
    
class Commentform(FlaskForm):
    comment = TextAreaField('Comment',validators=[Required()])
    submit = SubmitField('Post')
    
class Profileform(FlaskForm):
    bio = TextAreaField)("Describe yourself", validators=[Required()])
    submit = SubmitField('Submit')