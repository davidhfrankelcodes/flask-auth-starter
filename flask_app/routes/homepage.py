from flask import render_template, Blueprint
from dotenv import load_dotenv
import os
from dotenv import load_dotenv

load_dotenv()

SIGNUP_DISABLED = int(
    os.environ.get("FLASK_SIGNUP_DISABLED"))
    
homepage_bp = Blueprint('homepage', __name__)

@homepage_bp.route('/')
@homepage_bp.route('/home')
def homepage():
    return render_template(
        'homepage.html', 
        signup_disabled=SIGNUP_DISABLED,)
