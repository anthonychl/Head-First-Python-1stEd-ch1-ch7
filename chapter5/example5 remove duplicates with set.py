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


with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',') 

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',') 

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',') 

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

    
print( sorted(set( [sanitize(t) for t in james] )) [0:3])   
print( sorted(set( [sanitize(t) for t in julie] )) [0:3])   
print( sorted(set( [sanitize(t) for t in mikey] )) [0:3])   
print( sorted(set( [sanitize(t) for t in sarah] )) [0:3])   


