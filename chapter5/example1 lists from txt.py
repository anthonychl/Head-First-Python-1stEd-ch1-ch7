
"""
method chaining
the first method strip() is applied to the line in data and the result
of stripping is processed by the second method split()
creating a list. The methods are chained together to produce the required result

"""

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',') # method chaining

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',') 

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',') 

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

##print(james)
##print(julie)
##print(mikey)
##print(sarah)

#function chaining
print(sorted(james))    #copied sorting
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

