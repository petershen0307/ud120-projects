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

def quiz_execute(clf, features_train, labels_train, features_test, labels_test):
    train_start_time = time()

    #features_train = features_train[:len(features_train)//100]
    #labels_train = labels_train[:len(labels_train)//100]

    clf.fit(features_train, labels_train)
    train_end_time = time()
    print("time elapsed by training:", round(train_end_time - train_start_time, 3), "(s)")
    train_start_time = time()
    pred = clf.predict(features_test)
    print('how many 1 existed', sum(pred))
    train_end_time = time()
    print("time elapsed by predict:", round(train_end_time - train_start_time, 3), "(s)")
    print('predict score:', clf.score(features_test, labels_test))

cs = [10000.0]#[10.0, 100.0, 1000.0, 10000.0]
for c in cs:
    print('c is ', c)
    clf = SVC(kernel='rbf', C=c)
    quiz_execute(clf, features_train, labels_train, features_test, labels_test)
    print('\n')

#########################################################


