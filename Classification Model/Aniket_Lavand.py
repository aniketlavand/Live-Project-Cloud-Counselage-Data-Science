# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 22:26:15 2020

@author: ANIKET
"""


import numpy as np
import pandas as pd
import os
import sys

import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")
arg1 = sys.argv[1]

str=''
str = arg1
data=pd.read_csv(str)


df1=data.dropna(axis=1)

df3=df1[["Gender","Have you worked core Java","Have you worked on MySQL or Oracle database","Have you studied OOP Concepts","Label"]]
dummy_df=pd.get_dummies(df3,drop_first=True)



df1[["Gender","Have you worked core Java","Have you worked on MySQL or Oracle database","Have you studied OOP Concepts","Label"]]=dummy_df[["Gender_Male","Have you worked core Java_Yes","Have you worked on MySQL or Oracle database_Yes","Have you studied OOP Concepts_Yes","Label_ineligible"]]

                                                                                                                                        

df1['Label'] = df1['Label'].replace([1,0],[0,1])

df1["Programming Language Known other than Java (one major)"] = df1["Programming Language Known other than Java (one major)"].astype('category')




df1["other_lang"] = df1["Programming Language Known other than Java (one major)"].cat.codes




df1["Major/Area of Study"] = df1["Major/Area of Study"].astype('category')
df1["major"] = df1["Major/Area of Study"].cat.codes
df1['Which-year are you studying in?'] = df1['Which-year are you studying in?'].replace(['First-year','Second-year','Third-year','Fourth-year'],[1,2,3,4])

# # Data Split



X=df1[['Age','Gender','Which-year are you studying in?','CGPA/ percentage','Expected Graduation-year','Have you worked core Java','Have you worked on MySQL or Oracle database','Have you studied OOP Concepts','Rate your written communication skills [1-10]','other_lang','major']]
y=df1['Label']




from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,y, test_size=0.20,random_state=0)



# # Standardization




from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)


# # 1.Logistic Classification




from sklearn.linear_model import LogisticRegression 
lr = LogisticRegression(random_state = 0) 
lr.fit(X_train, y_train) 





y_pred = lr.predict(X_test) 




from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(y_test, y_pred) 
  




from sklearn.metrics import f1_score
lc=f1_score(y_pred, y_test)


# # svm



from sklearn import svm

#svm Classifier
clf = svm.SVC(kernel='rbf') # rbf Kernel


clf.fit(X_train, y_train)

#Predict the response for test dataset
sv=clf.score(X_test,y_test)


# # Decision Tree



from sklearn.tree import DecisionTreeClassifier
 
classifier = DecisionTreeClassifier(criterion='gini')
classifier.fit(X_train, y_train)
 
dtg=classifier.score(X_test, y_test)
 





classifier_entropy = DecisionTreeClassifier(criterion='entropy')
classifier_entropy.fit(X_train, y_train)
 
dte=classifier_entropy.score(X_test, y_test)


# # Random Forest



from sklearn.ensemble import RandomForestClassifier
 
classifier = RandomForestClassifier(n_estimators=100, criterion='gini')
classifier.fit(X_train, y_train)
 
rf=classifier.score(X_test, y_test)




best=max(lc,sv,dtg,dte,rf)
print(best)

