import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'movieImage'
})
export class MovieImagePipe implements PipeTransform {
  transform( text: string ): string {
    if( !text ){
      return 'https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg'
    } 
    return `https://image.tmdb.org/t/p/w185${text}`

  }
}
