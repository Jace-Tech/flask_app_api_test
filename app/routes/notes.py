from flask import Blueprint, request
from ..database import *
from ..utils.helpers import response, catch_exception, get_object_list, get_object

notes = Blueprint("notes", __name__)

@notes.get("/")
@catch_exception
def get_all_notes():
  all_notes = Note.find()
  return response("All notes", get_object_list(all_notes))


@notes.post("/")
@notes.post("/create")
@catch_exception
def create_notes():
  data = request.json
  result = Note.insert_one(data)

  if not result.acknowledged: raise Exception("Failed to create note")

  note = Note.find_one({"_id": result.inserted_id})
  return response("All notes", get_object(note))
