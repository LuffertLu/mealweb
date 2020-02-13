#resource model

from .. import db

#Model definition dependency
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Text, DateTime, Unicode, UnicodeText 

from sqlalchemy.orm import relationship, backref, session
import random
import os
import os.path as op

from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
#from redis import Redis
from wtforms import fields, widgets

from sqlalchemy.event import listens_for
from flask_admin import form




# Create directory for file fields to use
file_path = op.join(op.dirname(__file__), 'files')
try:
    os.mkdir(file_path)
except OSError:
    pass


# Create models
class File(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(64))
    path = Column(Unicode(128))

    def __unicode__(self):
        return self.name


class Image(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(64))
    path = Column(Unicode(128))

    def __unicode__(self):
        return self.name




class Page(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(64))
    text = Column(UnicodeText)

    def __unicode__(self):
        return self.name




# Delete hooks for models, delete files if models are getting deleted
@listens_for(File, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            # Don't care if was not deleted because it does not exist
            pass


@listens_for(Image, 'after_delete')
def del_image(mapper, connection, target):
    if target.path:
        # Delete image
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass

        # Delete thumbnail
        try:
            os.remove(op.join(file_path,
                              form.thumbgen_filename(target.path)))
        except OSError:
            pass


# define a custom wtforms widget and field.
# see https://wtforms.readthedocs.io/en/latest/widgets.html#custom-widgets
class CKTextAreaWidget(widgets.TextArea):
    def __call__(self, field, **kwargs):
        # add WYSIWYG class to existing classes
        existing_classes = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = '{} {}'.format(existing_classes, "ckeditor")
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextAreaField):
    widget = CKTextAreaWidget()








def build_sample_db():
    """
    Populate a small db with some example entries.
    """

    import random
    import string

    db.drop_all()
    db.create_all()

 
    images = ["Buffalo", "Elephant", "Leopard", "Lion", "Rhino"]
    for name in images:
        image = Image()
        image.name = name
        image.path = name.lower() + ".jpg"
        db.session.add(image)

    for i in [1, 2, 3]:
        file = File()
        file.name = "Example " + str(i)
        file.path = "example_" + str(i) + ".pdf"
        db.session.add(file)

    sample_text = "<h2>This is a test</h2>" + \
    "<p>Create HTML content in a text area field with the help of <i>WTForms</i> and <i>CKEditor</i>.</p>"
    db.session.add(Page(name="Test Page", text=sample_text))

    db.session.commit()
    return


