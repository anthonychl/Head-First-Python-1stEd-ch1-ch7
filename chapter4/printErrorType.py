#ejemplo1
try:
    data = open('missing.txt')
    print(data.readline(),end='')
    
except IOError as err: #giving a name:'err' to the exception object 
    print('Error', str(err)) #use str() to force err to a string
    
finally:
    if 'data' in locals():#the in operator tests for membership
        data.close()

#print(locals())

#ejemplo2
try:
   with open('its.txt','w') as data:
       print("its sdfk ..", file=data)
    
except IOError as err: 
    print('Error', str(err))

        
