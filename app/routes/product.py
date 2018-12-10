from app import app
from app.models.Product import Product
from app.decorators.check_bearerToken import token_required
from flask import json, jsonify, request, Response
from app.helpers.error_funcs import invalid_request_method, invalid_request_headers
from sqlalchemy.exc import SQLAlchemyError



@app.route("/products", methods=['GET', 'POST'])
def products_Index():
  if request.method == 'GET':
    return get_all_products()
  elif request.method == 'POST':
    return create_product()
  else:
    return invalid_request_method()



@app.route('/products/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def productsById(id):
  if request.method == 'GET':
    return get_product_byId(id)
  elif request.method == 'PATCH':
    return edit_product_byId(id)
  elif request.method == 'DELETE':
    return delete_product_byId(id)
  else:
    return invalid_request_method()



@token_required
def get_all_products():
  products = Product.find()
  context = {
    "success" : True,
    "message" : "Fetch All Products",
    "data" : []
  }
  for product in products:
    context['data'].append(product.toDict_WithRelations())
  response = jsonify(context)
  return response, 200



@token_required
def create_product():
  header_content_type = request.headers.get("Content-Type")
  statusCode = 201
  context = {
    "success" : True,
    "message" : "Create New Product",
    "data" : None
  }
  if header_content_type == 'application/json':
    product = Product(name=request.json["name"], details=request.json["details"])
  elif header_content_type =='application/x-www-form-urlencoded':
    product = Product(name=request.form["name"], details=request.form["details"])
    
  try :
    product.create()
    context["data"] = product.toDict_WithRelations()
  except SQLAlchemyError as e:
    context['success'] = False
    context['message'] = str(e.__dict__['orig'])
    statusCode = 500
  return jsonify(context), statusCode



@token_required
def get_product_byId(id):
  product = Product.findById(id)
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Get Product By ID",
    "data" : {}
  }
  if product is not None:
    context['data'] = product.toDict_WithRelations()
  else:
    context['success'] = False
    context['message'] = "Product Doesn't Exist"
    statusCode = 404
  return jsonify(context), statusCode



@token_required
def edit_product_byId(id):
  product = Product.findById(id)
  statusCode = 200
  header_content_type = request.headers.get("Content-Type")
  context = {
    "success" : True,
    "message" : "Update Product By ID",
    "data" : None
  }
  if product is not None:
    if header_content_type == 'application/json':
      product.name = request.json['name']
      product.details = request.json['details']
    elif header_content_type =='application/x-www-form-urlencoded':
      product.name = request.form['name']
      product.details = request.form['details']
    else:
      return invalid_request_headers()
    product.update()
    product = Product.findById(id)
    context['data'] = product.toDict_WithRelations()
  else:
    context['success'] = False
    context['message'] = "Product Doesn't Exist"
    statusCode = 404
    
  return jsonify(context), statusCode



@token_required
def delete_product_byId(id):
  product = Product.findById(id)
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Delete Product By ID",
  }
  if product is not None:
    product.delete()
  else:
    context['success'] = False
    context['message'] = "Product Doesn't Exist"
    statusCode = 404
  return jsonify(context), statusCode