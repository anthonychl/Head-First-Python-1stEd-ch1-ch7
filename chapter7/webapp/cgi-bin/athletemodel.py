import pickle
from athletelist import AthleteList

def get_coach_data(filename): 
    try:
        with open(filename) as fn:
            data = fn.readline()
        templ = data.strip().split(',')
        return AthleteList(templ.pop(0),templ.pop(0),templ)
    except IOError as ioe:
        print('IOError: '+str(ioe))
        return(None)

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file) #take each file and turn it into an AthleteList object instance, and add the data to the dictionary
        all_athletes[ath.name] = ath #Each athlete's name is used as the 'key' and the 'value' is the AthleteList object instance
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print('File error (put_to_store) '+ str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes = pickle.load(athf) #read the entire file into the dictionary
    except IOError as ioerr:
        print('File error (get_from_store) '+ str(ioerr))
    return(all_athletes)
            



