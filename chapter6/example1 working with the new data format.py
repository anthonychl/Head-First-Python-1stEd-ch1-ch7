"""
manejar el nuevo formato de los datos: "nombre,fechaDeNacimiento,tiempo1,tiempo2,...,tiempoN" 
crear lista sin duplicados y mostrar los tres mejores tiempos
"""

def sanitize(time_string):
    if '-' in time_string:  
        splitter = '-'
    elif ':' in time_string: 
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


def get_coach_data(filename): #i renamed the function 'createListFromFile' so it will match the books name
    try:
        with open(filename) as fn:
            data = fn.readline()
        return data.strip().split(',')
    except IOError as ioe:
        print('IOError: '+str(ioe))
        return(None) 



sarah = get_coach_data('sarah2.txt')
(sarah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)
print( sarah_name+"'s fastest times are: "+str( sorted(set( [sanitize(t) for t in sarah] )) [0:3]) )  

james = get_coach_data('james2.txt')
(james_name,james_dob) = james.pop(0),james.pop(0)
print( james_name+"'s fastest times are: "+str( sorted(set( [sanitize(t) for t in james] )) [0:3]) )

julie = get_coach_data('julie2.txt')
(julie_name,julie_dob) = julie.pop(0),julie.pop(0)
print( julie_name+"'s fastest times are: "+str( sorted(set( [sanitize(t) for t in julie] )) [0:3]) )  

mikey = get_coach_data('mikey2.txt')
(mikey_name,mikey_dob) = mikey.pop(0),mikey.pop(0)
print( mikey_name+"'s fastest times are: "+str( sorted(set( [sanitize(t) for t in mikey] )) [0:3]) )
