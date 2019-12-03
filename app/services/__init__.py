#!/usr/bin/env python3
# encoding: utf-8
from flask import Blueprint

services = Blueprint('services', __name__)

from . import views, forms