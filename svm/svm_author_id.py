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
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
from sklearn import svm
#clf = svm.SVC(kernel='linear')
clf = svm.SVC(kernel='rbf',C=10000.0)
clf.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
predictions=clf.predict(features_test)

import numpy as np
print np.count_nonzero(predictions)
#print predictions[10]
#print predictions[26]
#print predictions[50]
#pred2=clf.predict([features_test[26]])
#pred3=clf.predict([features_test[50]])
print "predicting time:", round(time()-t1, 3), "s"

print clf.score(features_test, labels_test)


#########################################################


