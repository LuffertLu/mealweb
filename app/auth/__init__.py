#!/usr/bin/env python3
# encoding: utf-8
from flask import Blueprint

auth = Blueprint('auth', __name__)
#auth = Blueprint('auth', __name__, template_folder='template/auth', static_folder='static/auth', url_prefix='/auth')

from . import views, forms