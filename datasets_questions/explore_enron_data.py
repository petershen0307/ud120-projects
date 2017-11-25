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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print("how many data points (ex: people) are in enron dataset: {}".format(len(enron_data)))
# print(enron_data.keys())
# print(enron_data['METTS MARK'])
print("how many features are available? {}".format(len(enron_data['METTS MARK'])))

poiCount = 0
for person, info in enron_data.items():
    if info["poi"]:
        poiCount += 1
print("How many POIs are there in the E+F dataset? {}".format(poiCount))
