import { Component, OnInit } from '@angular/core';
import { RestService } from '../../service/rest.service';
import { Info } from '../../interfaces/info-movies.interfaces';

@Component({
  selector: 'app-info-movie',
  templateUrl: './info-movie.component.html',
  styleUrls: ['./info-movie.component.css'],
})
export class InfoMovieComponent implements OnInit {

  public movie?: Info;
  public idMovieI!: number;
  constructor(private RestService: RestService  ) {}
  ngOnInit(): void {
  }

}
