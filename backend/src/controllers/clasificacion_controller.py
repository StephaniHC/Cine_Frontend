from flask import Blueprint, request, jsonify
from models.clasificacion_model import Clasificacion

clasificacion_bp = Blueprint('clasificacion', __name__)

@clasificacion_bp.route('/createClasificacion', methods=['POST'])
def create_clasificacion():
    data = request.get_json()
    required_fields = ['nombre', 'sigla']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'Campo "{field}" es obligatorio.'}), 400

    try:
        result = Clasificacion.create(
            nombre=data['nombre'],
            sigla=data['sigla']
        )
        if isinstance(result, Clasificacion):
            clasificacion = result
            return jsonify({'message': 'Clasificación creada exitosamente.', 'clasificacion_id': clasificacion.id}), 201
        else:
            error_message = result[1]
            return jsonify({'message': f'Error al crear la clasificación: {error_message}'}), 500 
    except Exception as e:
        return jsonify({'message': f'Error al crear la clasificación: {str(e)}'}), 500

    
@clasificacion_bp.route('/getClasificaciones', methods=['GET'])
def get_clasificaciones():
    clasificaciones = Clasificacion.get_all()
    detalles_clasificaciones = [{'nombre': clasificacion['nombre'], 'sigla': clasificacion['sigla']} for clasificacion in clasificaciones]
    
    return jsonify({'clasificaciones': detalles_clasificaciones})