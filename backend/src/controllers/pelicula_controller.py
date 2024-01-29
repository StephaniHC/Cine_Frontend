from flask import Blueprint, request, jsonify
from models.pelicula_model import Pelicula 

pelicula_bp = Blueprint('pelicula', __name__) 
    
@pelicula_bp.route('/createPelicula', methods=['POST'])
def create_pelicula():
    data = request.get_json() 
    required_fields = ['nombre', 'fecha_estreno', 'sinopsis', 'portada', 'genero_id', 'clasificacion_id']
     
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'Campo "{field}" es obligatorio.'}), 400
    try:
        result = Pelicula.create(
        nombre=data['nombre'],
        fecha_estreno=data['fecha_estreno'],
        sinopsis=data['sinopsis'],
        portada=data['portada'],
        genero_id=data['genero_id'],
        clasificacion_id=data['clasificacion_id']
        )

        if isinstance(result, Pelicula):
            pelicula = result
            return jsonify({'message': 'Película creada exitosamente.', 'pelicula_id': pelicula.id}), 201
        else:
            error_message = result[1]
            return jsonify({'message': f'Error al crear la película: {error_message}'}), 500

    except Exception as e:
        return jsonify({'message': f'Error al crear la película: {str(e)}'}), 500


@pelicula_bp.route('/getPeliculaDetails', methods=['GET'])
def get_pelicula_details():
    peliculas = Pelicula.get_details()

    detalles_peliculas = [
        {
            'nombre': pelicula['nombre'],
            'fecha_estreno': pelicula['fecha_estreno'],
            'sinopsis': pelicula['sinopsis'],
            'portada': pelicula['portada'],
            'genero_id': pelicula['genero_id'],
            'clasificacion_id': pelicula['clasificacion_id']
        }
        for pelicula in peliculas
    ]

    return jsonify({'peliculas': detalles_peliculas})

@pelicula_bp.route('/getPeliculasByGenero/<int:genero_id>', methods=['GET'])
def get_peliculas_by_genero(genero_id):
    try:
        peliculas = Pelicula.get_by_genero(genero_id)
        return jsonify({'peliculas': peliculas}), 200
    except Exception as e:
        return jsonify({'message': f'Error al obtener películas por género: {str(e)}'}), 500
