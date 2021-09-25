from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    email = StringField("Email", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired()])
    submit_button = SubmitField("Let me join")


class LoginForm(FlaskForm):
    email = StringField("Email", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired()])
    submit_button = SubmitField("Let me in")


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment")
    submit = SubmitField("comment")
