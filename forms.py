from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField(
        validators=[Email("Некорректный email")],
        render_kw={"class_": "field", "placeholder": "Почта"})
    password = PasswordField(
        validators=[DataRequired(), Length(min=8, max=25, message="Пароль должен быть от 8 до 25 символов")],
        render_kw={"class": "field", "placeholder": "Пароль"})
    remindme = BooleanField(default=False)
    submit = SubmitField("Войти")


class RegisterForm(FlaskForm):
    email = StringField(
        validators=[Email("Введите корректный email")],
        render_kw={"class": "field", "placeholder": "Почта"})

    name = StringField(
        validators=[Length(min=2, max=25, message="Имя должно быть от 2 до 25 символов")],
        render_kw={"class": "field", "placeholder": "Имя"})

    password = PasswordField(
        validators=[DataRequired(), Length(min=8, max=25, message="Пароль должен быть от 8 до символов")],
        render_kw={"class": "field", "placeholder": "********"})
    password1 = PasswordField(
        validators=[DataRequired(), EqualTo('password', message="Пароли не совпадают")],
        render_kw={"class": "field", "placeholder": "********"})
    submit = SubmitField("Регистрация")
