from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods = ['GET'])
def main() -> str:
   return 'Currency Converter'

