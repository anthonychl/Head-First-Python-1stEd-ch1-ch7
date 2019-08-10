import pickle

with open('mydata.pickle','wb') as mysavedata: #wb write, binary mode
    pickle.dump([1,2,'three'],mysavedata)   #save to file

with open('mydata.pickle','rb') as myrestoredata: #rb read, binary mode
    a_list = pickle.load(myrestoredata)     #read from file

print(a_list)
