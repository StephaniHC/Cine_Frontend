from database.db_singleton import Database

class Pelicula: 
    def __init__(self, id, nombre, fecha_estreno, portada, clasificacion_id, genero_id, sinopsis):
        self.id = id
        self.nombre = nombre
        self.fecha_estreno = fecha_estreno
        self.sinopsis = sinopsis
        self.portada = portada
        self.genero_id = genero_id 
        self.clasificacion_id = clasificacion_id
    
    @staticmethod   
    def create(nombre, fecha_estreno, sinopsis, portada, genero_id, clasificacion_id): 
        try:
            db = Database()
            connection = db.connection 
            cursor = connection.cursor(dictionary=True) 
            cursor.execute("INSERT INTO pelicula (nombre, fecha_estreno, sinopsis, portada, genero_id, clasificacion_id) VALUES (%s, %s, %s, %s, %s, %s)",
                        (nombre, fecha_estreno, sinopsis, portada, genero_id, clasificacion_id))
            
            connection.commit()
            last_row_id = cursor.lastrowid  
            return Pelicula(id= last_row_id, nombre=nombre, fecha_estreno=fecha_estreno, sinopsis=sinopsis, portada=portada, genero_id=genero_id, clasificacion_id=clasificacion_id)
            
        except Exception as e:
            connection.rollback()  
            return False, str(e)
        finally:
            cursor.close()

    @staticmethod
    def get_details():
        db = Database()
        connection = db.connection

        cursor = connection.cursor(dictionary=True) 
        cursor.execute("""
            SELECT 
                pelicula.nombre,
                pelicula.portada,
                pelicula.fecha_estreno,
                pelicula.sinopsis,
                genero.id AS genero_id,
                clasificacion.id AS clasificacion_id
            FROM pelicula
            JOIN genero ON pelicula.genero_id = genero.id
            JOIN clasificacion ON pelicula.clasificacion_id = clasificacion.id
        """)
        peliculas = cursor.fetchall() 
        cursor.close() 
        return peliculas
    
    @staticmethod
    def get_by_genero(genero_id):
        try:
            db = Database()
            connection = db.connection
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT * FROM pelicula WHERE genero_id = %s", (genero_id,))
            peliculas = cursor.fetchall()

            return peliculas
        except Exception as e:
            raise Exception(f'Error al obtener películas por género: {str(e)}')
        finally:
            cursor.close()
     