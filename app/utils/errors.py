from functools import wraps
from .helpers import response

class CustomRequestError(Exception):
  """
    Request error class
  """
  def __init__(self, message, code = 400):
    super().__init__(message)
    self.message = message
    self.code = code


def catch_exception(fn):
  @wraps(fn) 
  def wrapper(*args, **kwargs):
    gamer = "JACE"
    try:
      return fn(*args, **kwargs)
    
    except CustomRequestError as e:
      return response(e.message, None, False), e.code
  
    except Exception as e:
      return response(str(e), None, False), 500
  return wrapper