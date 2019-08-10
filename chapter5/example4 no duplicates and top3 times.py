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

    
james = sorted( [sanitize(t) for t in james] )    
julie = sorted( [sanitize(t) for t in julie] )
mikey = sorted( [sanitize(t) for t in mikey] )
sarah = sorted( [sanitize(t) for t in sarah] )

unique_james = []
unique_julie = []
unique_mikey = []
unique_sarah = []

for each_t in james:
    if each_t not in unique_james:      #if the data IS NOT in the new list
        unique_james.append(each_t)     #append the unique data to the new list

for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)

for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)

for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)

print(unique_james[0:3]) #print from 0 upto but not including 3
print(unique_julie[0:3])
print(unique_mikey[0:3])
print(unique_sarah[0:3])
