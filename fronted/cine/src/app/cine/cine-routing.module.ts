import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LayoutPageComponent } from './layout/layout-page/layout-page.component';
import { ListMoviesComponent } from './pages/list-movies/list-movies.component'; 
import { CreateMovieComponent } from './pages/create-movies/create-movies.component'; 
import { InfoMovieComponent } from './pages/info-movie/info-movie.component'; 

const routes: Routes = [
  {
    path: '',
    component: LayoutPageComponent,
    children: [
      { path: 'list-movies', component: ListMoviesComponent }, 
      { path: 'create-movies', component: CreateMovieComponent }, 
      { path: 'info/:id', component: InfoMovieComponent }, 
      { path: '**', redirectTo: 'list-movies' },
    ],
  },
];
@NgModule({
  imports: [RouterModule.forChild( routes )],
  exports: [ RouterModule ],
})
export class CineRoutingModule {}
