import athletemodel
import yate
import cgi #cgi library

athletes = athletemodel.get_from_store() # get the data from the model and put it into a dictionary

form_data = cgi.FieldStorage() #Grab all of the form data and put it in a dictionary
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach kelly's Timing data"))
print(yate.header("Athlete: "+athlete_name+', DOB: '+athletes[athlete_name].dob))
print(yate.para("The top 3 times are: "))
print(yate.u_list(athletes[athlete_name].top3()))
print(yate.include_footer({"Home":"/index.html","Select another athlete":"generate_list.py"}))

