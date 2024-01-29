Es un proyecto de prueba con las tecnologias de mysql, python, flask, angular
Primeramente se debe de crear la base de datos en la parte del backend se encuentra el script de la bd
Luego crear un archivo con las credenciales de las mismas en la parte del backend en la carpeta de config
se crea un archivo config.py y se pone las credenciales de la bd como se muestra a continuacion:
# config/config.py
DB_CONFIG = {
    'DB_HOST': '',
    'DB_USER': '',
    'DB_PASSWORD': '',
    'DB_NAME': '',
}
Para ejecutar el backend se debe de crear el entorno virtual
- pip install virtualenv (en caso de no tener instalado)
-  python -m venv venv (o el nombre que se le vea adecuado)
Se debe de instalar las dependencias, en este caso se las encuentra en el archivo requirements.txt
una vez instaladas las dependencias se procede a ejecutar el archivo app.py
Para ejecutar el frontend se debe de ejecutar el siguiente comando para instalar als dependencias
- npm install
  luego de instalar las dependencias se debe de ejecutar el siguiente comando
- ng serve
el backend se ejecuta en el puerto : 5000
y el frontend en el puerto: 4200
