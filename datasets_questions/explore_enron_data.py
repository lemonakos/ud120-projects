#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pprint
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "The size of the dataset is: %d" % len(enron_data)

record = enron_data["SKILLING JEFFREY K"].keys()

print "The number of features is: %d" % len(record)

pprint.pprint(enron_data)
#print enron_data["ALLEN PHILLIP K"]["poi"]

poi = []
for v in enron_data.values():
    poi.append(v["poi"])
    
print poi.count(True)