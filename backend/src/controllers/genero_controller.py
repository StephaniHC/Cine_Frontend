from flask import Blueprint, request, jsonify
from models.genero_model import Genero

genero_bp = Blueprint('genero', __name__)

@genero_bp.route('/createGenero', methods=['POST'])
def create_genero():
    data = request.get_json()
    required_fields = ['nombre']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'Campo "{field}" es obligatorio.'}), 400

    try:
        result = Genero.create(
            nombre=data['nombre']
        ) 
        
        if isinstance(result, Genero):
            genero = result
            return jsonify({'message': 'Género creada exitosamente.', 'genero_id': genero.id}), 201
        else:
            error_message = result[1]
            return jsonify({'message': f'Error al crear la Género: {error_message}'}), 500 
    except Exception as e:
        return jsonify({'message': f'Error al crear el género: {str(e)}'}), 500

    
@genero_bp.route('/getGeneros', methods=['GET'])
def get_generos():
    generos = Genero.get_all()
    nombres_generos = [genero['nombre'] for genero in generos]

    return jsonify({'generos': nombres_generos})