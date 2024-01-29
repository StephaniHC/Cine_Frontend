import mysql.connector
from mysql.connector import pooling
from flask import Flask

class Database:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            if app:
                cls._instance.init_app(app)
        return cls._instance


    def init_app(self, app: Flask):
        db_config = {
            "host": app.config['DB_HOST'],
            "user": app.config['DB_USER'],
            "password": app.config['DB_PASSWORD'],
            "database": app.config['DB_NAME'],
        }

        self.pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)
         
    @property
    def connection(self):
        return self.pool.get_connection()
