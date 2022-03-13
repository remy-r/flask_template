"""Auth Module"""

from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    Response,
)
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login() -> str:
    """Login route"""
    return render_template("login.html")


@auth.route("/logout")
def logout() -> str:
    """Logout route"""
    return "<p>Logout</p>"


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up() -> Response:
    """Sign-up route"""
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if email is not None and len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif first_name is not None and len(first_name) < 2:
            flash("First Name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        elif password1 is not None and len(password1) < 7:
            flash("Password must be greater than 6 character.", category="error")
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method="sha256"),
            )
            db.session.add(new_user)
            db.session.commit()

            flash("Account created !", category="success")
            return redirect(url_for("views.home"))
    return render_template("sign_up.html")
