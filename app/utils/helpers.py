from functools import wraps

def response(msg: str, data=None, success=True):
  return { "message": msg, "data": data, "success": success }
