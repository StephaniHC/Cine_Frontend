export interface Soon {
  dates:         Dates; 
  results:       ResultP[]; 
  total_results: number;
}

export interface Dates {
  date: Date; 
}
  
export interface ResultP { 
  backdrop_path:     string;
  genre_ids:         number[];
  id:                number;
  poster_path:       string;
  title:             string;
}
