from flask.ext.wtf import Form
from wtforms.fields import TextField
from wtforms.validators import Required

class TODOFORM(Form):
	label = TextField('label', validators = [Required()])