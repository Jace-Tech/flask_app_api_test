from functools import wraps

def response(msg: str, data=None, success=True):
  return { "message": msg, "data": data, "success": success }

def get_object(obj):
  new_data = {}
  for key, val in obj.items():
    new_data[key] = str(val)
  return new_data

def get_object_list(seq):
  return [get_object(data) for data in seq]

def catch_exception(fn):
  @wraps(fn) 
  def wrapper(*args, **kwargs):
    try:
      return fn(*args, **kwargs)
    except Exception as e:
      return response(str(e), None, False)
  return wrapper