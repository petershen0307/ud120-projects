#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn.svm import SVC

clf = SVC(kernel='linear')
train_start_time = time()
clf.fit(features_train, labels_train)
train_end_time = time()
print("time elapsed by training:", round(train_end_time - train_start_time, 3), "(s)")
train_start_time = time()
print(clf.predict(features_test))
train_end_time = time()
print("time elapsed by predict:", round(train_end_time - train_start_time, 3), "(s)")
print('predict score:', clf.score(features_test, labels_test))
#########################################################


