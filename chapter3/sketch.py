#solution 1
import os
if os.path.exists('sketch.txt'):
    data = open('sketch.txt')
    for each_line in data:
        if not each_line.find(':')==-1:
            (role, line_spoken) = each_line.split(':',1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
       
    data.close()
else:
    print('The datafile is missing')


#solution 2, faster & easier to implement and read, less complex
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except:
            pass

    data.close()
except:
    print('The datafile is missing')

#solution 2.1, taking the exception handlin from 'generic' to 'specific'
#so the program no longer silently ignore other errors
#so we can know about them and handle later on
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print('The datafile is missing')

