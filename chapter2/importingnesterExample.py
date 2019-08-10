###One way to do it
##import nester
##
##starwars = ['the last jedi','the force awakens']
##
##movies = [starwars,'black panther','avengers']
##
##nester.print_lol(movies)

#another way to do it
from nester import print_lol

starwars = ['the last jedi','the force awakens']

movies = [starwars,'black panther','avengers']

print_lol(movies)


"""
you need to be careful. If you already have
a function called print_lol defined in your current namespace, the
specific import statement (from nester import print_lol)
overwrites your function with the imported
one, which might not be the behavior you want
"""
