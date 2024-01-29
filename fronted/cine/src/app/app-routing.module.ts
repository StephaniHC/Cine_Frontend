import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'movie',
    loadChildren: () => import('./cine/cine.module').then( modulo => modulo.StarMovieModule)
  },
  {
    path: '**',
    redirectTo: 'movie'
  } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
