from database.db_singleton import Database

class Clasificacion:
    def __init__(self, id, nombre, sigla):
        self.id = id
        self.nombre = nombre 
        self.sigla = sigla 
        
    @staticmethod
    def create(nombre, sigla):
        try:
            db = Database()
            connection = db.connection
            cursor = connection.cursor(dictionary=True)

            cursor.execute("INSERT INTO clasificacion (nombre, sigla) VALUES (%s, %s)",
                           (nombre, sigla))

            connection.commit()
            last_row_id = cursor.lastrowid
            return Clasificacion(last_row_id, nombre, sigla)
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
        cursor.execute("SELECT nombre, sigla FROM clasificacion")
        clasificaciones = cursor.fetchall()
        cursor.close()

        return clasificaciones
