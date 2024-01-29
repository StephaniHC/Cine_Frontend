import { RestService } from '../../service/rest.service';
import { ResultM } from '../../interfaces/top-movies.interfaces';
import { Component, Input, OnInit } from '@angular/core';
import { ResultList } from '../../interfaces/list-movies.interfaces';
import { ResultP } from '../../interfaces/create-movies.interface';

@Component({
  selector: 'star-card-movie',
  templateUrl: './card-movie.component.html',
  styleUrls: ['./card-movie.component.css']
})
export class CardMovieComponent implements OnInit {
 
  @Input()
  public moviesReceived!: ResultM |  ResultP

  ngOnInit(): void { 
    if( !this.moviesReceived ) throw new Error('la lista es requerida')
  } 
}
