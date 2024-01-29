
CREATE DATABASE bd_prueba;
USE bd_prueba;  
-- Crear la tabla Pelicula
CREATE TABLE Pelicula (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    fecha_estreno DATE,
    sinopsis TEXT,
    portada VARCHAR(255)
);
-- Crear la tabla Genero
CREATE TABLE Genero (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30)
);
-- Crear la tabla Clasificacion
CREATE TABLE Clasificacion (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    sigla VARCHAR(20)
);
-- Establecer la relación de 1 a muchos entre Pelicula y Genero
ALTER TABLE Pelicula
ADD COLUMN genero_id INT,
ADD CONSTRAINT fk_pelicula_genero
    FOREIGN KEY (genero_id)
    REFERENCES Genero(Id);
-- Establecer la relación de 1 a 1 entre Pelicula y Clasificacion
ALTER TABLE Pelicula
ADD COLUMN clasificacion_id INT,
ADD CONSTRAINT fk_pelicula_clasificacion
    FOREIGN KEY (clasificacion_id)
    REFERENCES Clasificacion(Id);  