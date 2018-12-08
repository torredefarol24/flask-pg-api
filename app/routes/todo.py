from app import flaskPgJwtApp
from app.models.Todo import Todo
from flask import json, Response, request, jsonify
from app.decorators.check_bearerToken import token_required



@flaskPgJwtApp.route("/todos", methods=['GET', 'POST'])
def todos_Create_ReadAll():
  if request.method == 'POST':
    return create_todo()
  elif request.method == 'GET':
    return get_all_todos()
  else:
    return invalid_request_method()



@flaskPgJwtApp.route("/todos/<int:id>", methods=['GET', 'PATCH', 'DELETE'])
def todos_Read_Update_Delete(id):
  if request.method =='GET':
    return get_todo_byId(id)
  elif request.method == 'PATCH':
    return edit_todo_byId(id)
  elif request.method == 'DELETE':
    return delete_todo_byId(id)
  else:
    return invalid_request_method()



def get_all_todos():
  todos = Todo.query.order_by("id desc").all()
  context = {
    "success" : True,
    "message" : "Todos Fetched",
    "data" : []
  }
  for todo in todos:
   context["data"].append(todo.toDict())
  resp_data = json.dumps(context)
  response = Response(resp_data, status=200)
  return response



@token_required
def create_todo():
  header_content_type = request.headers.get('Content-Type')
  statusCode = 201
  context = {
    "success" : True,
    "message" : "Create Todo",
  }
  if header_content_type == 'application/json':
    context['data'] = request.json
    todo = Todo(title=request.json["title"])
    todo.create()
  elif header_content_type == 'application/x-www-form-urlencoded':
    context["data"] = request.form
    todo = Todo(title=request.form["title"])
    todo.create()
  else:
    context['message'] = "Invalid Headers"
    context["success"] = False
    statusCode = 500
  response = jsonify(context)
  return response, statusCode



def get_todo_byId(id):
  todo = Todo.query.get(id)
  context = {
    "success" : True,
    "message" : "Fetch Todo By Id",
    "data" : None
  }
  if (todo):
    context["data"] = todo.toDict()
  else:
    context["success"] = False
    context["message"] = "Todo not Found"
  respData = json.dumps(context)
  response = Response(respData, status=200)
  return response



@token_required
def edit_todo_byId(id):
  todo = Todo.query.get(id)
  header_content_type = request.headers.get('Content-Type')
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Update Todo By Id",
  }
  if todo and header_content_type == 'application/json':
    context['data'] = request.json
    todo.title = request.json["title"]
    todo.save()
  elif todo and header_content_type == 'application/x-www-form-urlencoded':
    context["data"] = request.form
    todo.title = request.form["title"]
    todo.save()
  elif not Todo:
    context["data"] = None
    context["success"] = False
    context["message"] = "Todo Not Found"
  else:
    context['message'] = "Invalid Headers"
    context["success"] = False
    statusCode = 500
  response = jsonify(context)
  return response, statusCode  



@token_required
def delete_todo_byId(id):
  todo = Todo.query.get(id)
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Delete Todo By Id",
  }
  if todo:
    todo.delete()
  else:
    context['message'] = "Todo Not Found"
    context["success"] = False
    statusCode = 500
  response = jsonify(result=context)
  return response, statusCode



def invalid_request_method():
  context = {
    "success" : False,
    "data" : None,
    "message" : "Invalid Request Method"
  }
  return jsonify(error = context), 500