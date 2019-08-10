###first modification, print data
##man = []  #assign an empty list to man and other
##other = []
##try:
##    data = open('sketch.txt')
##    for each_line in data:
##        try:
##            (role, line_spoken) = each_line.split(':',1)
##            line_spoken = line_spoken.strip() #strip() removes unwanted whitespace fron a string
##            if role == 'Man':
##                man.append(line_spoken)
##            elif role == 'Other Man':
##                other.append(line_spoken)
##        except ValueError:
##            pass
##
##    data.close()
##except IOError:
##    print('The datafile is missing')
##
##print(man)
##print(other)

#--------------------------------------------------------------

###second modification, saving the data
##man = []  
##other = []
##try:
##    data = open('sketch.txt')
##    for each_line in data:
##        try:
##            (role, line_spoken) = each_line.split(':',1)
##            line_spoken = line_spoken.strip() 
##            if role == 'Man':
##                man.append(line_spoken)
##            elif role == 'Other Man':
##                other.append(line_spoken)
##        except ValueError:
##            pass
##
##    data.close()
##except IOError:
##    print('The datafile is missing')
##
##try:
##    manfile = open("man_data.txt","w")
##    otherfile = open("other_data.txt","w")
##    
##    print(man, file=manfile)
##    print(other, file=otherfile)
##
##except IOError:
##    print("Error con los archivos")
##
##finally: #if no errors occur any code within finally executes, and if an error occurs the exception suite runs and then the finally suite runs    
##    manfile.close()   #we want to make sure the files always close, if we put this two lines at the end of the 'try:' block, and an error occurs they wont execute    
##    otherfile.close() 

#--------------------------------------------------------------

###third modification, check locals()
##man = []  
##other = []
##try:
##    data = open('sketch.txt')
##    for each_line in data:
##        try:
##            (role, line_spoken) = each_line.split(':',1)
##            line_spoken = line_spoken.strip() 
##            if role == 'Man':
##                man.append(line_spoken)
##            elif role == 'Other Man':
##                other.append(line_spoken)
##        except ValueError:
##            pass
##
##    data.close()
##except IOError:
##    print('The datafile is missing')
##
##try:
##    manfile = open("man_data.txt","w")
##    otherfile = open("other_data.txt","w")
##    
##    print(man, file=manfile)
##    print(other, file=otherfile)
##
##except IOError:
##    print("Error con los archivos")
##
##finally: 
##    if manfile in locals():
##        manfile.close()   
##    if manfile in locals():
##        otherfile.close()

#--------------------------------------------------------------

###fourth modification, using 'with' , no need for 'finally:'
##man = []  
##other = []
##try:
##    data = open('sketch.txt')
##    for each_line in data:
##        try:
##            (role, line_spoken) = each_line.split(':',1)
##            line_spoken = line_spoken.strip() 
##            if role == 'Man':
##                man.append(line_spoken)
##            elif role == 'Other Man':
##                other.append(line_spoken)
##        except ValueError:
##            pass
##
##    data.close()
##except IOError:
##    print('The datafile is missing')
##
##try:
####    with open("man_data.txt","w") as manfile:
####        print(man, file=manfile)
####        
####    with open("other_data.txt","w") as otherfile:
####        print(other, file=otherfile)
##
##    #or we can combine the two with statements into one
##    with open("man_data.txt","w") as manfile,open("other_data.txt","w") as otherfile:
##        print(man, file=manfile)
##        print(other, file=otherfile)
##
##except IOError as err:
##    print("Error :" + str(err))

#--------------------------------------------------------------

###fifth modification, using 'nester' module
##
##from nester import print_lol
##
##man = []  
##other = []
##try:
##    data = open('sketch.txt')
##    for each_line in data:
##        try:
##            (role, line_spoken) = each_line.split(':',1)
##            line_spoken = line_spoken.strip() 
##            if role == 'Man':
##                man.append(line_spoken)
##            elif role == 'Other Man':
##                other.append(line_spoken)
##        except ValueError:
##            pass
##
##    data.close()
##except IOError:
##    print('The datafile is missing')
##
##try:
##    with open("man_data.txt","w") as manfile,open("other_data.txt","w") as otherfile:
##        print_lol(man, fh=manfile) #fh es el nombre del argumento en print_lol en nester
##        print_lol(other, fh=otherfile)
##
##except IOError as err:
##    print("Error :" + str(err))

#--------------------------------------------------------------

#sixth modification, using 'pickle' module

import pickle #<----

man = []  
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip() 
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()
except IOError:
    print('The datafile is missing')

try:
    with open("man_data_pickle.txt","wb") as manfile,open("other_data_pickle.txt","wb") as otherfile:
        pickle.dump(man,manfile) 
        pickle.dump(other,otherfile)

except IOError as err:
    print("IO Error :" + str(err))

except pickle.PickleError as perr:
    print("Pickle Error :" + str(perr))



