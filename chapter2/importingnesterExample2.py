#importando nester despues de haberlo actualizado a nester 1.3.0

import nester

starwars = ['the last jedi','the force awakens']

movies = [starwars,'black panther','avengers']

nester.print_lol(movies,True,1)

nester.print_lol(movies) #sin utilizar los otros parametros, asi q usa los valores por defecto

