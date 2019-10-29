#Internal dependency


#Flask related dependency
from flask import Blueprint

#Database related dependency


main = Blueprint('main', __name__, url_prefix='')

from . import views, errors, forms

