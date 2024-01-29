import { Component, OnInit, Input } from '@angular/core';
import { ResultList } from '../../interfaces/list-movies.interfaces';

@Component({
  selector: 'star-card-top',
  templateUrl: './card-top.component.html',
  styleUrls: ['./card-top.component.css']
})
export class CardTopComponent implements OnInit {
 
  @Input()
  public moviesTopReceived!: ResultList

  ngOnInit(): void { 
    if( !this.moviesTopReceived ) throw new Error('La lista es requerida')
  } 
}
