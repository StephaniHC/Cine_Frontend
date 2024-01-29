from database.db_singleton import Database

class Genero:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre 
        
    @staticmethod
    def create(nombre):
        try:
            db = Database()
            connection = db.connection
            cursor = connection.cursor(dictionary=True)

            cursor.execute("INSERT INTO genero (nombre) VALUES (%s)",
                           (nombre,))

            connection.commit()
            last_row_id = cursor.lastrowid
            return Genero(last_row_id, nombre)
        except Exception as e:
            connection.rollback()
            return False, str(e)
        finally:
            cursor.close()
            
    @staticmethod 
    def get_all():
        db = Database()
        connection = db.connection

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT nombre FROM genero")
        generos = cursor.fetchall()
        cursor.close()

        return generos