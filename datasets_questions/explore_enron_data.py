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
# print(next (iter (enron_data.values())))
print("how many features are available? {}".format(len(next (iter (enron_data.values())))))

poiCount = 0
for person, info in enron_data.items():
    if info["poi"]:
        poiCount += 1
print("How many POIs are there in the E+F dataset? {}".format(poiCount))
# miss understand the quesion quiz 16
# allEnronName = enron_data.keys()
# import re
# nameListWithPOI = 0
# with open("../final_project/poi_names.txt", "r") as f:
#     for line in f:
#         match = re.findall("[^\\((y|n)\\) ]{1}[a-zA-Z, ]+", line)
#         if match != []:
#             name = match[0].replace(",", "")
#             print(name)
#             for enronName in allEnronName:
#                 if name.upper() in enronName.upper():
#                     nameListWithPOI += 1
#         else:
#             print(line)
# print("How Many POIs Exist? {}".format(nameListWithPOI))

def findKeyInEnronData(enronData, name):
    keyName = None
    for enronName in enronData.keys():
        if name.upper() in enronName.upper():
            keyName = enronName
            break
    return keyName

name = "Prentice James"
keyName = findKeyInEnronData(enron_data, name)
# print(keyName)
# totalStockOfJamesPrentice = enron_data[keyName]["exercised_stock_options"] + enron_data[keyName]["restricted_stock"]
print("What is the total value of the stock belonging to James Prentice? \
{}".format(enron_data[keyName]["total_stock_value"]))

name = "Colwell Wesley"
keyName = findKeyInEnronData(enron_data, name)
# for k, v in enron_data[keyName].items():
#     print("{}: {}".format(k, v))
# len([x for x in enron_data[keyName].values() if x != 'NaN'])
print("How many email messages do we have from Wesley Colwell to persons of interest? \
{}".format(enron_data[keyName]["from_this_person_to_poi"]))

keyName = findKeyInEnronData(enron_data, "Skilling Jeffrey K")
# print(keyName)
print("What’s the value of stock options exercised by Jeffrey K Skilling? \
{}".format(enron_data[keyName]["exercised_stock_options"]))

# quiz 25 follow the money "total_payments"
keyName = findKeyInEnronData(enron_data, "Skilling Jeffrey")
# print(keyName, enron_data[keyName])

keyName = findKeyInEnronData(enron_data, "Lay Kenneth")
# print(keyName, enron_data[keyName])

keyName = findKeyInEnronData(enron_data, "Fastow Andrew")
# print(keyName, enron_data[keyName])

# quiz 27 Dealing with Unfilled Features
qualifySalary = 0
knownEmail = 0
for _, v in enron_data.items():
    if str(v["salary"]).upper() != "NaN".upper():
        qualifySalary += 1
    if v["email_address"].upper() != "NaN".upper():
        knownEmail += 1
print("qualify salary: {}".format(qualifySalary))
print("known email: {}".format(knownEmail))

# quiz 29 How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?

import sys
sys.path.append("../tools/")
from feature_format import featureFormat

featureList = featureFormat(enron_data, ["total_payments"])
print("total payments without NaN {}".format(len(featureList)))
print("percentage of without NaN: {}".format(len(featureList)/len(enron_data)))

featureList = featureFormat(enron_data, ["total_payments", "poi"])
countPOIWithoutNaNTotalPay = 0
for ele in featureList:
    if ele[1] == 1:
        countPOIWithoutNaNTotalPay += 1
print("total payments of POI without NaN {}".format(countPOIWithoutNaNTotalPay))
print("percentage of POI without NaN: {}".format(countPOIWithoutNaNTotalPay/poiCount))
