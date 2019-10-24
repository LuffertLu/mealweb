from flask import Flask,render_template,request

@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>Not found</h3>'), 404
