from flask import Flask
from dotenv import dotenv_values

ENV = dotenv_values()

def create_app():
  app = Flask(__name__)

  # CONFIGS HERE
  app.config["APP_SECRET"] = ENV['APP_SECRET']
  app.config["MONGODB_URI"] = ENV['MONGODB_URI']

  # ROUTES
  from .routes.notes import notes
  app.register_blueprint(notes, url_prefix="/api/v1/notes")

  return app