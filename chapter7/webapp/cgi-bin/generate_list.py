import athletemodel
import yate
import glob #this module lets you query your operating system for a list of file names

data_files = glob.glob("data/*.txt") #creating a list of the file names of type '*.txt' within folder 'data'
athletes = athletemodel.put_to_store(data_files) #creating a dictionary of athletes from the list of data files

print(yate.start_response()) #always start with a Content-type line
print(yate.include_header("Coach Kelly's List of Athletes")) #provide a title for the page

print(yate.start_form("generate_timing_data.py")) #start generating the form providing the name of the server-side program to link to.
print(yate.para("Select an athlete from the list to work with:"))

for each_athlete in athletes: #generate a radio button for each athlete
    print(yate.radio_button("which_athlete",athletes[each_athlete].name))

print(yate.end_form("Select")) # end the form with a custom text for the submit button

print(yate.include_footer({"Home":"/index.html"}))  # a link to go back to the Home page



