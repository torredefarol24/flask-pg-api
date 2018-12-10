from app import app
from app.models.Order import Order
from app.models.Product import Product
from app.decorators.check_bearerToken import token_required
from app.helpers.error_funcs import invalid_request_headers, invalid_request_method
from sqlalchemy.exc import SQLAlchemyError
from flask import json, request, jsonify
from datetime import datetime


@app.route("/orders", methods=['GET', 'POST'])
def orders_Index():
  if request.method == 'GET':
    return get_all_orders()
  elif request.method == 'POST':
    return create_order()
  else:
    return invalid_request_method()



@app.route("/orders/<int:id>", methods=['GET', 'PATCH', 'DELETE'])
def orders_WithId(id):
  if request.method == 'GET':
    return get_order_byId(id)
  elif request.method == 'PATCH':
    return edit_order_byId(id)
  elif request.method =='DELETE':
    return delete_order_byId(id)
  else:
    return invalid_request_method()



@token_required
def get_all_orders():
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Get All Orders",
    "data" : []
  }
  orders = Order.find()
  for order in orders:
    context['data'].append(order.toDict_WithRelations())
  return jsonify(context), statusCode



@token_required
def get_order_byId(id):
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Get Order by Id",
    "data" : None
  }
  order = Order.findById(id)
  if order:
    context['data'] = order.toDict_WithRelations()
  else:
    context['success'] = False
    context['message'] = "Order Doesn't Exist"
  return jsonify(context), statusCode



@token_required
def edit_order_byId(id):
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Edit Order by Id",
    "data" : None
  }
  request_header_json = request.headers.get('Content-Type') == 'application/json'
  request_header_form = request.headers.get('Content-Type') == 'application/x-www-form-urlencoded'
  update_order = False
  
  order = Order.findById(id)
  if order and request_header_json:
    order.status = request.json['status']
    update_order = True
  elif order and request_header_form:
    order.status = request.form['status']
    update_order = True
  elif order and not (request_header_form or request_header_json):
    return invalid_request_headers()
  elif not order:
    context['message'] = "Order Doesn't Exist"
    context['success'] = False
    statusCode = 404
  
  if update_order:
    order.update()
    order = Order.findById(id)
    context['data'] = order.toDict_WithRelations()

  return jsonify(context), statusCode



@token_required
def delete_order_byId(id):
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Delete Order by Id",
    "data" : None
  }
  order = Order.findById(id)
  if order:
    order.delete()
  else:
    context['message'] = "Order Doesn't Exist"
    context['success'] = False
    statusCode = 404
  return jsonify(context), statusCode



@token_required
def create_order():
  statusCode = 201
  context = {
    "success" : True,
    "message" : "Create Order wtith Multiple Products",
    "data" : []
  }
  request_header_json = request.headers.get('Content-Type') == 'application/json'
  request_header_form = request.headers.get('Content-Type') == 'application/x-www-form-urlencoded'

  if request_header_json:
    order = Order(user_id=request.json['user_id'], created_at=datetime.now(), status="Order Created")
  elif request_header_form:
    order = Order(user_id=request.form['user_id'], created_at=datetime.now(), status="Order Created")
  else:
    return invalid_request_headers()
    
  for id in request.json['product_ids']:
    product = Product.findById(id)
    order.products.append(product)
  order.create()
  context['data'] = order.toDict_WithRelations()
  return jsonify(context), statusCode