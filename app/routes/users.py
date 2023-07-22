from flask import Blueprint, request
from ..utils.errors import catch_exception, CustomRequestError
from ..utils.helpers import response
from ..database import get_connection
from ..database.user_table import get_user_by_id

users = Blueprint("users", __name__)

@users.post("/")
@catch_exception
def create_user():
  db = get_connection()
  if not db : raise CustomRequestError("Couldn't connect to database", 500)

  connection, cursor = get_connection()
  data = request.get_json()

  print("DATA:", data)

  query = "INSERT INTO user (email, password) VALUES (%s, %s)"
  cursor.execute(query, (data.get('email'), data.get('password')))
  connection.commit()

  # CHECK IF USER WAS CREATED
  last_id = cursor.lastrowid
  if not last_id:
    raise CustomRequestError("Failed to add user", 500)

  # GET USERS DATA
  user = get_user_by_id(last_id)
  connection.close()

  return response("User created!", user), 201