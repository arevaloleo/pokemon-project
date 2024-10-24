from flask import Blueprint, jsonify, request
from ..services.pokemon_service import PokemonService
from ..services.middleware_service import MiddlewareService
from authorizer import token_required

pokemon_bp = Blueprint('pokemon', __name__) # se modulariza por medio de flask agrupando las rutas
pokemon_service = PokemonService()
middleware = MiddlewareService()
@pokemon_bp.route('/pokemon/<string:name>', methods=['GET'])
@token_required
def pokemon_by_name(name):
    data = pokemon_service.get_pokemon_by_name(name)
    return jsonify(data)


@pokemon_bp.route('/pokemon/azar', methods=['GET'])
@token_required
def random_pokemon_type():
    filter_query = request.args.get('type', '')
    print(filter_query)
    
    data = pokemon_service.random_pokemon_type_filter(filter_query)
    return jsonify(data)

@pokemon_bp.route('/pokemon/long-name', methods=['GET'])
@token_required
def random_pokemon_long_name():
    filter_query = request.args.get('type', '')
    print(filter_query) 
    data = pokemon_service.long_name(filter_query)
    return jsonify(data)

@pokemon_bp.route('/pokemon', methods=['GET'])
@token_required
def filter_pokemon_by_iam():
    filter_query = request.args.get('filter', '')
    print(filter_query)
    data = middleware.obtener_pokemon_por_clima()
    return jsonify(data)
