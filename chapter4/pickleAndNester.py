import pickle
import nester


a_list = []

try:
    with open('man_data_pickle.txt','rb') as data: #rb read, binary mode
        a_list = pickle.load(data)     #read from file

except IOError as err:
    print("IO Error :" + str(err))

except pickle.PickleError as perr:
    print("Pickle Error :" + str(perr))
    
nester.print_lol(a_list)


##shorter version of program above
##with open('man_data_pickle.txt','rb') as myrestoredata: #rb read, binary mode
##    a_list = pickle.load(myrestoredata)     #read from file
##
##nester.print_lol(a_list)
