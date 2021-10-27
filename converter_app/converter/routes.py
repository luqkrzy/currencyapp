from flask import Blueprint

conv = Blueprint('conv', __name__)

@conv.route('/api/convert/')
def hello_world():
   return "Here's converter"
