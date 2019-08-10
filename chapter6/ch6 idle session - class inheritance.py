Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class NamedList(list): #provide the name of the class that this new subclass derives from
	def __init__(self,a_name):
		list.__init__([])
		self.name = a_name

		
>>> johnny = NamedList("john Paul Jones") #new NamedList object instance
>>> type(johnny)
<class '__main__.NamedList'>
>>> dir(johnny)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'name', 'pop', 'remove', 'reverse', 'sort']
>>> #johnny can do everything a list can, as well as store data in the 'name' attribute
>>> johnny.append("Bass Player")
>>> johnny.extend(['Composer','Arranger','Musician'])
>>> johnny
['Bass Player', 'Composer', 'Arranger', 'Musician']
>>> johnny.name
'john Paul Jones'
>>> #because johnny is a list is ok to do list-typer things to it
>>> for attr in johnny:
	print(johnny.name + "is a " + attr +".")

	
john Paul Jonesis a Bass Player.
john Paul Jonesis a Composer.
john Paul Jonesis a Arranger.
john Paul Jonesis a Musician.
>>> 
