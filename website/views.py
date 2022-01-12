from flask import Blueprint, render_template, request
from website.models import Item
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
    # Get all the items when you load the home page
    return render_template("base.html")

@views.route('/create', methods = ['GET', 'POST'])
def home():
    # Get all the items when you load the home page
    return render_template("create.html")


@views.route('/export')
def export():
    # Get all the items when you load the home page
    return "<h1>export</h1>"  