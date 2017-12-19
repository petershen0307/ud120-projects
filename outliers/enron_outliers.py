#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
# quiz 17
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)

### your code below
def drawScatterPlot(data):
    for point in data:
        salary = point[0]
        bonus = point[1]
        matplotlib.pyplot.scatter( salary, bonus )
    matplotlib.pyplot.xlabel("salary")
    matplotlib.pyplot.ylabel("bonus")
    matplotlib.pyplot.show()

# quiz 15, 16
for k, v in data_dict.items():
    if (v['salary'] == 26704229):
        print(k, v['salary'])
drawScatterPlot(data)
