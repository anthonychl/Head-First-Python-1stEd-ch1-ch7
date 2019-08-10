"""
crear lista sin duplicados y mostrar los tres mejores tiempos
"""

def sanitize(time_string):
    if '-' in time_string:  #use the 'in' operator to check if the string containes a dash
        splitter = '-'
    elif ':' in time_string: #use the 'in' operator to check if the string containes a colon
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


def createListFromFile(filename):
    try:
        with open(filename) as fn:
            data = fn.readline()
        return data.strip().split(',')
    except IOError as ioe:
        print('IOError: '+str(ioe))
        return(None) #return 'None' to indicate failure
    

james = createListFromFile('james.txt')
julie = createListFromFile('julie.txt')
mikey = createListFromFile('mikey.txt')
sarah = createListFromFile('sarah.txt')

print( sorted(set( [sanitize(t) for t in james] )) [0:3])   
print( sorted(set( [sanitize(t) for t in julie] )) [0:3])   
print( sorted(set( [sanitize(t) for t in mikey] )) [0:3])   
print( sorted(set( [sanitize(t) for t in sarah] )) [0:3])   


