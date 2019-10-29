#Flask related dependency
from flask import Blueprint

#Database related dependency

main = Blueprint('main', __name__, url_prefix='')

#Internal dependency
from . import views, errors, forms