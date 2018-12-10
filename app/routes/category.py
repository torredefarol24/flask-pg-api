from app import app
from app.models.Category import Category
from app.models.Product import Product
# from app.decorators.check_bearerToken import jwt_required
from app.helpers.error_funcs import invalid_request_headers, invalid_request_method
from sqlalchemy.exc import SQLAlchemyError
from flask import request, jsonify 
from flask_jwt_extended import jwt_required


@app.route("/category", methods=['GET', 'POST'])
def category_index():
  if request.method == 'GET':
    return get_all_categories()
  elif request.method == 'POST':
    return create_category()
  else:
    return invalid_request_method()



@app.route("/category/<int:id>", methods=['GET', 'PATCH', 'DELETE'])
def category_WithId(id):
  if request.method == 'GET':
    return get_category_byId(id)
  elif request.method == 'PATCH':
    return edit_category_byId(id)
  elif request.method == 'DELETE':
    return delete_category_byId(id)
  else:
    return invalid_request_method()


None
@jwt_required
def get_all_categories():
  categs = Category.find()
  statusCode = 200
  context = {
    "message" : "Get All Categories",
    "success" : True,
    "data" : []
  }
  for categ in categs:
    context['data'].append(categ.toDict_WithRelations())
  return jsonify(context), statusCode



@jwt_required
def create_category():
  context = {
    "success" : True,
    "message" : "Create Category",
    "data" : None
  }
  statusCode = 200
  request_header_json = request.headers.get("Content-Type") == 'application/json'
  request_header_form = request.headers.get("Content-Type") == 'appliactoin/x-www-form-urlencoded'

  if request_header_json:
    categ = Category(name=request.json['name'])
  elif request_header_form:
    categ = Category(name=request.form['name'])
  else:
    return invalid_request_headers()
  categ.create()
  context['data'] = categ.toDict_WithRelations()
  return jsonify(context),statusCode



@jwt_required
def get_category_byId(id):
  categ = Category.findById(id)
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Get Category by Id",
    "data" : None
  }
  if categ: 
    context['data'] = categ.toDict_WithRelations()
  else :
    context['success'] = False
    context['message'] = "Category Doesn't Exist"
    statusCode = 404
  return jsonify(context), statusCode



@jwt_required
def edit_category_byId(id):
  categ = Category.findById(id)
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Edit Category by Id",
    "data" : None
  }
  request_header_json = request.headers.get("Content-Type") == "application/json"
  request_header_form = request.headers.get("Content-Type") == "application/x-www-form-urlencoded"
  if categ and request_header_json: 
    categ.name = request.json['name']
  elif categ and request_header_form:
    categ.name = request.form['name']
  elif categ and not (request_header_form or request_header_json):
    return invalid_request_headers()
  elif not categ:
    context['success'] = False
    context['message'] = "Category Doesn't Exist"
    statusCode = 404
    return jsonify(context), statusCode
  
  categ.update()
  categ = Category.findById(id)
  context['data'] = categ.toDict_WithRelations()
  return jsonify(context), statusCode



@jwt_required
def delete_category_byId(id):
  categ = Category.findById(id)
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Delete Category by Id",
    "data" : None
  }
  if categ :
    categ.delete()
  else:
    context['success'] = False
    context['message'] = "Category Doesn't Exist"
    statusCode = 404
  return jsonify(context), statusCode



@app.route("/category/product/assign", methods=['POST'])
@jwt_required
def assign_product_to_categ():
  statusCode = 200
  context = {
    "message" : "Assign Category to Product",
    "success" : True,
    "data" : []
  }
  request_header_json = request.headers.get("Content-Type") == 'application/json'
  request_header_form = request.headers.get("Content-Type") == 'appliactoin/x-www-form-urlencoded'

  if request_header_json:
    categ = Category.findById(request.json['category_id']) 
  elif request_header_form:
    categ = Category.findById(request.form['category_id'])
  else:
    return invalid_request_headers()

  if categ and request_header_json:  
    for id in request.json['product_ids']:
      product = Product.findById(id)
      categ.products.append(product)
  elif categ and request_header_form:
    for id in request.form['product_ids']:
      product = Product.findById(id)
      categ.products.append(product)
  elif not categ:
    context['success'] = False,
    context['message'] = "Category Not Found"
    statusCode = 404
    return jsonify(context), statusCode

  categ.update()
  context['data'] = categ.toDict_WithRelations()
  return jsonify(context), statusCode
