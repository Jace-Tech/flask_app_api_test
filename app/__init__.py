from flask import Flask
from dotenv import dotenv_values
from .utils.helpers import response

ENV = dotenv_values()

def create_app():
  app = Flask(__name__)

  # ***** CONFIGS *****
  
  # APP CONFIGS
  app.config["APP_SECRET"] = ENV['APP_SECRET']
  app.config["MONGODB_URI"] = ENV['MONGODB_URI']

  # MAIL CONFIGS
  app.config['MAIL_SERVER'] = ENV["MAIL_SERVER"]
  app.config['MAIL_PORT'] = ENV["MAIL_PORT"]
  app.config['MAIL_USE_SSL'] = True
  app.config['MAIL_USERNAME'] = ENV["MAIL_USERNAME"]
  app.config['MAIL_PASSWORD'] = ENV["MAIL_PASSWORD"]

  # ***** ROUTES *****
  from .routes.notes import notes
  app.register_blueprint(notes, url_prefix="/api/v1/notes")

  from .routes.users import users
  app.register_blueprint(users, url_prefix="/api/v1/users")

  # ERROR ROUTES
  app.errorhandler(404)
  def invalid_route():
    return response("Invalid route", None, False)
  
  app.errorhandler(500)
  def server_error():
    return response("Something went wrong, please try again", None, False)

  return app