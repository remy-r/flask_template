"""View Module"""

from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
def home() -> str:
    """Home root"""
    return render_template("home.html")
