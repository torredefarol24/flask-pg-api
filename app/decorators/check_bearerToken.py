from functools import wraps
import json
from flask import Response, request



def unAuthorizedError():
  statusCode = 401
  context = {
    "success" : False,
    "message" : "Auth Required"
  }
  respData = json.dumps(context)
  response = Response(respData, status=statusCode)
  return response



def token_required(f):
  @wraps(f)
  def decoratedFunc(*args, **kwargs):
    token = request.headers.get('Authorization')
    
    if not token:
      return unAuthorizedError()
    
    return f(*args, **kwargs)
  
  return decoratedFunc


