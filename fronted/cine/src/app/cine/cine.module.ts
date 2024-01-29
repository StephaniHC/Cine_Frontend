import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
 
import { InfoMovieComponent } from './pages/info-movie/info-movie.component';
import { ListMoviesComponent } from './pages/list-movies/list-movies.component'; 
import { CreateMovieComponent } from './pages/create-movies/create-movies.component'; 
import { LayoutPageComponent } from './layout/layout-page/layout-page.component';
import { CineRoutingModule } from './cine-routing.module'; 
import { MovieImagePipe } from './pipes/movie-image.pipe';
import { CardMovieComponent } from './components/card-movie/card-movie.component';
import { MovieTextPipe } from './pipes/movie-title.pipe';  
import { MovieDesciptionPipe } from './pipes/movie-description.pipe';
import { CardTopComponent } from './components/card-top/card-top.component';
import { ReactiveFormsModule } from '@angular/forms'; 



@NgModule({
  declarations: [
    ListMoviesComponent,
    InfoMovieComponent, 
    CreateMovieComponent, 
    LayoutPageComponent, 
    MovieImagePipe,
    CardMovieComponent,
    MovieTextPipe, 
    MovieDesciptionPipe,
    CardTopComponent
  ],
  imports: [
    CommonModule,
    CineRoutingModule,
    ReactiveFormsModule

  ]
})
export class StarMovieModule { }
