#!/usr/bin/env python3
# encoding: utf-8

#Internal dependency
from . import mail

#Flask related dependency
from flask import Flask, current_app, render_template
from flask_mail import Mail, Message

#Other related dependency
from threading import Thread

#Initialization start 
def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)


def send_email(to, subject, template, **kwargs):
	app = current_app._get_current_object()
	msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX'] + ' ' + subject, 
					sender = app.config['FLASK_MAIL_SENDER'], recipients = [to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	thr = Thread(target = send_async_email, args = [app, msg])
	thr.start()
	return thr