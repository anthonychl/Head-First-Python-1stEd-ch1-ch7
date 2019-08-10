"""
    update the get_coach_data() function to return a dictionary instead of a list
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

##this is how i modified it
##def get_coach_data(filename): 
##    try:
##        with open(filename) as fn:
##            data = fn.readline()
##        ls = data.strip().split(',')
##        dct = {}
##        dct['Name'] = ls.pop(0)
##        dct['DOB'] = ls.pop(0)
##        dct['Times'] = ls
##        dct['Top3'] = str( sorted(set( [sanitize(t) for t in dct['Times']] )) [0:3])
##        return dct
##    except IOError as ioe:
##        print('IOError: '+str(ioe))
##        return(None)

##this is how the function is modified in the book
def get_coach_data(filename): 
    try:
        with open(filename) as fn:
            data = fn.readline()
        templ = data.strip().split(',')
        return {'Name':templ.pop(0),'DOB':templ.pop(0),'Times':str( sorted(set( [sanitize(t) for t in templ] )) [0:3])}
    except IOError as ioe:
        print('IOError: '+str(ioe))
        return(None)




mikey = get_coach_data('mikey2.txt')
print( mikey['Name']+"'s fastest times are: "+mikey['Times'])

james = get_coach_data('james2.txt')
print( james['Name']+"'s fastest times are: "+james['Times'])

julie = get_coach_data('julie2.txt')
print( julie['Name']+"'s fastest times are: "+julie['Times'])

sarah = get_coach_data('sarah2.txt')
print( sarah['Name']+"'s fastest times are: "+sarah['Times'])

















