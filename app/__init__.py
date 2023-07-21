from flask import Flask
from dotenv import dotenv_values
from .utils.helpers import response

ENV = dotenv_values()

def create_app():
  app = Flask(__name__)

  # CONFIGS HERE
  app.config["APP_SECRET"] = ENV['APP_SECRET']
  app.config["MONGODB_URI"] = ENV['MONGODB_URI']

  # ROUTES
  from .routes.notes import notes
  app.register_blueprint(notes, url_prefix="/api/v1/notes")

  # ERROR ROUTES
  app.errorhandler(404)
  def invalid_route():
    return response("Invalid route", None, False)
  
  app.errorhandler(500)
  def server_error():
    return response("Something went wrong, please try again", None, False)

  return app