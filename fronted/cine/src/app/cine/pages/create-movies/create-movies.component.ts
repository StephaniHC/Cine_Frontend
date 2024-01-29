import { Component, OnInit } from '@angular/core';
import { RestService } from '../../service/rest.service'; 

@Component({
  selector: 'app-create-movies',
  templateUrl: './create-movies.component.html',
  styleUrls: ['./create-movies.component.css']
})
export class CreateMovieComponent implements OnInit {
  pelicula = {
    nombre: "",
    fecha_estreno: "",
    sinopsis: "",
    portada: "",
    genero_id: 0,
    clasificacion_id: 0
  }
  generos: any[] = [];
  constructor( private restService: RestService){}
  crearPelicula(): void { 
    const info = { 
      nombre: this.pelicula.nombre,
      fecha_estreno: this.pelicula.fecha_estreno,
      sinopsis: this.pelicula.sinopsis,
      portada: this.pelicula.portada,
      genero_id: this.pelicula.genero_id,
      clasificacion_id: this.pelicula.clasificacion_id
    }; 
    this.restService.PostRequest('/pelicula/createPelicula', info).subscribe(
        (response) => {
            console.log('Respuesta del backend:', response);
        },
        (error) => {
            console.error('Error en la solicitud:', error);
        }
    );


}

  ngOnInit(): void { 
    
  }
}
