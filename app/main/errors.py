#!/usr/bin/env python3
# encoding: utf-8
from . import main


@main.errorhandler(404)
def page_not_found(exc):
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500
