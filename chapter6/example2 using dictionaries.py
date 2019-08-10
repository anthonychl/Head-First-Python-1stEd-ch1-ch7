"""
manejar el nuevo formato de los datos: "nombre,fechaDeNacimiento,tiempo1,tiempo2,...,tiempoN" 
usar diccionarios
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



mdata = get_coach_data('mikey2.txt')
mikey = {}
mikey['Name'] = mdata.pop(0)
mikey['DOB'] = mdata.pop(0)
mikey['Times'] = mdata
print( mikey['Name']+"'s fastest times are: "+str( sorted(set( [sanitize(t) for t in mikey['Times']] )) [0:3]) )

jdata = get_coach_data('james2.txt')
james = {}
james['Name'] = jdata.pop(0)
james['DOB'] = jdata.pop(0)
james['Times'] = jdata
print( james['Name']+"'s fastest times are: "+str( sorted(set( [sanitize(t) for t in james['Times']] )) [0:3]) )

judata = get_coach_data('julie2.txt')
julie = {}
julie['Name'] = judata.pop(0)
julie['DOB'] = judata.pop(0)
julie['Times'] = judata
print( julie['Name']+"'s fastest times are: "+str( sorted(set( [sanitize(t) for t in julie['Times']] )) [0:3]) )

sdata = get_coach_data('sarah2.txt')
sarah = {}
sarah['Name'] = sdata.pop(0)
sarah['DOB'] = sdata.pop(0)
sarah['Times'] = sdata
print( sarah['Name']+"'s fastest times are: "+str( sorted(set( [sanitize(t) for t in sarah['Times']] )) [0:3]) )

















