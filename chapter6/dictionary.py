#two ways of creating an empty dictionary
cleese = {}  
palin = dict()

#checking that they are in fact dictionaries, using type()
print( type(cleese) )
print( type(palin) )

#this is how to add data to the dictionary
cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor','comedian','writer','film producer']

palin = {'Name': 'Michael Palin', 'Occupations': ['comedian','actor','writer','tv']}


#accessing the data
print( palin['Name'] )

print( cleese['Occupations'] )
print( cleese['Occupations'][0] )  # use numbers to access a list item stored at a particular dictionary key 
print( cleese['Occupations'][-1] ) # -1 the last of the occupations, -2 second to last ...


#as with lists, a python dictionary can grow dynamically to store additional key/value pairings
palin['Birthplace'] = "Bromhill, Sheffield, England"

cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England"


#unlike lists, dictionaries dont maintain insertion order,
#the dictionary maintains the associations not the ordering, dont worry it doesnt matter :)
print( palin )

print( cleese )
