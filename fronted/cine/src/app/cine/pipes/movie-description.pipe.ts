import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'movieDescription'
})
export class MovieDesciptionPipe implements PipeTransform {
  transform(text: string): string {
    if( text.length > 240){
      let textoReducido = text.substring(0, 220)
      return textoReducido += '.'
    }

    return text
  }
}
