from flask import Blueprint, request, current_app
from ..utils.helpers import response, get_object_list, get_object
from ..utils.errors import catch_exception, CustomRequestError
from ..utils.mailer import send_mail


notes = Blueprint("notes", __name__)


@notes.post("/send")
@catch_exception
def email():
  data = request.get_json()
  if not send_mail(current_app, data.get('subject'), [data.get('email')], data.get('message')):
    raise CustomRequestError("Could not send", 500)
  return response("Message sent", None)


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
