from app import flaskPgJwtApp
from app.models.Todo import Todo
from flask import json, Response, request, jsonify
from app.decorators.check_bearerToken import token_required

@flaskPgJwtApp.route("/todos", methods=['GET', 'POST'])
def todosIndex():
  if request.method == 'POST':
    return create_todo()
  else:
    return get_all_todos()



def get_all_todos():
  todos = Todo.query.all()
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
    todo.save()
  elif header_content_type == 'application/x-www-form-urlencoded':
    context["data"] = request.form
    todo = Todo(title=request.form["title"])
    todo.save()
  else:
    context['message'] = "Invalid Headers"
    context["success"] = False
    statusCode = 500
  response = jsonify(context)
  return response, statusCode



@flaskPgJwtApp.route("/todos/<int:id>")
def get_todo_byId(id):
  todo = Todo.query.get(id)
  context = {
    "success" : True,
    "message" : "Fetch Todo By Id",
    "data" : todo.toDict()
  }
