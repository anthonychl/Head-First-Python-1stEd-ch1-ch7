Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Athlete:
	def __init__(self,a_name,a_dob=None,a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

		
>>> sarah = Athlete('Sarah Sweeney','2002-6-17',['2.58','2.58','1.56'])
>>> james = Athlete('James Jones')
>>> type(sarah)
<class '__main__.Athlete'>
>>> type(james)
<class '__main__.Athlete'>
>>> sarah
<__main__.Athlete object at 0x000000C3600EC748>
>>> james
<__main__.Athlete object at 0x000000C3600ECA20>
>>> sarah.name
'Sarah Sweeney'
>>> james.dob
>>> james.times
[]
>>> sarah.times
['2.58', '2.58', '1.56']
>>> 
