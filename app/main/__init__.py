#Flask related dependency
from flask import Blueprint

#Database related dependency

main = Blueprint('main', __name__)

from . import views, forms, errors