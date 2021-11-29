# CODE by @ancoder
import flask
from flask import (
  Flask,
  request,
  abort,
  render_template,
  url_for,
  redirect
)
import configparser

app = Flask(__name__, template_folder="html")

@app.before_request
def before():
  config = configparser.ConfigParser()
  if config["SERVER"]["SERVER_DOWN"] == 'true':
    return render_template("servers-down.html")
  else:
    pass
  
app.run("0.0.0.0")