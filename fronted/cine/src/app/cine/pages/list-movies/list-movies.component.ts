import { Component, OnInit } from '@angular/core';
import { RestService } from '../../service/rest.service';
import { ResultM } from '../../interfaces/top-movies.interfaces';

@Component({
  selector: 'app-list-movies',
  templateUrl: './list-movies.component.html',
  styleUrls: ['./list-movies.component.css'],
})
export class ListMoviesComponent implements OnInit { 
  public listMovies!: ResultM[]; 

  constructor(private RestService: RestService) {}

  ngOnInit(): void { 
  }
 
}
