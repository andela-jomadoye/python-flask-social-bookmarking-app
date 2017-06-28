from flask_wtf import Form
from wtforms.fields import StringField
from flask.ext.wtf.html5 import URLField
from wtforms.validators import DataRequired, url


class BookmarkForm(Form):
    jedUrl = URLField('jedUrl', validators=[DataRequired(), url()])
    description = StringField('description')
