from pymongo import MongoClient
from flask import current_app
from dotenv import dotenv_values

ENV = dotenv_values()

def create_db():
  try:
    connection = MongoClient(ENV["MONGODB_URI"])
    db = connection['flask']
    return db
  
  except Exception as e:
    print("Error:", str(e)) 
    print("Error creating database") 



# MODELS
Note = create_db()['note']