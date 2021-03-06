#!/usr/bin/python

"""
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)


### the input features we want to use
### can be any key in the person-level dictionary (salary, director_fees, etc.)
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
feature_4 = "from_messages"
feature_poi  = "poi"
features_list = [feature_poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

def l9Q22():
    f = [e for _, e in finance_features if e != 0]
    print("l9Q22 ", feature_2, " maximum:", max(f))
    print("l9Q22 ", feature_2, " minimum:", min(f))
l9Q22()

def l9Q23():
    f = [s for s, _ in finance_features if s != 0]
    print("l9Q23 ", feature_1, " maximum:", max(f))
    print("l9Q23 ", feature_1, " minimum:", min(f))
l9Q23()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
def l9Q20():
    features_list = [feature_poi, feature_1, feature_2]
    data = featureFormat(data_dict, features_list )
    poi, finance_features = targetFeatureSplit( data )
    return KMeans(n_clusters=2).fit_predict(finance_features), "clusters_L9Q20.pdf", finance_features

def l9Q21():
    features_list = [feature_poi, feature_1, feature_2, feature_3]
    data = featureFormat(data_dict, features_list )
    poi, finance_features = targetFeatureSplit( data )
    return KMeans(n_clusters=3).fit_predict(finance_features), "clusters_L9Q21.pdf", finance_features

from sklearn.preprocessing import MinMaxScaler
def l9Q24():
    features_list = [feature_poi, feature_1, feature_2]
    data = featureFormat(data_dict, features_list )
    poi, finance_features = targetFeatureSplit( data )
    fe = [e for _, e in finance_features]
    fs = [s for s, _ in finance_features]
    newFeatures = []
    scaler = MinMaxScaler()
    scaler.fit(finance_features)
    finance_features = scaler.transform(finance_features)
    print("l10Q16 scale value (200000, 1000000):", scaler.transform([[200000, 1000000]]))
    return KMeans(n_clusters=2).fit_predict(finance_features), "clusters_L9Q24.pdf", finance_features

def l10Q17():
    features_list = [feature_poi, feature_1, feature_4]
    data = featureFormat(data_dict, features_list )
    poi, finance_features = targetFeatureSplit( data )
    for f1, f4 in finance_features:
        plt.scatter( f1, f4 )
    plt.show()
    # fe = [e for _, e in finance_features]
    # fs = [s for s, _ in finance_features]
    # newFeatures = []
    # scaler = MinMaxScaler()
    # scaler.fit(finance_features)
    # finance_features = scaler.transform(finance_features)
    # return KMeans(n_clusters=2).fit_predict(finance_features), "clusters_L10Q17.pdf", finance_features
l10Q17()
# pred, outputName, finance_features = l9Q24()

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name=outputName, f1_name=feature_1, f2_name=feature_2)
except NameError:
    print("no predictions object named pred found, no clusters to plot")
