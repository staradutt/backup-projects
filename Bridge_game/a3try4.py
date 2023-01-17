import numpy as np
import pandas as pd
import sklearn
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import joblib
file = open("a3x.csv", 'r')
cards = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}
hands = []

for line in file.readlines():
	s1 = [0 for i in range(13)]
	s2 = [0 for i in range(13)]
	s3 = [0 for i in range(13)]
	s4 = [0 for i in range(13)]
	seq = line.split('.')
	for ch in seq[0]:
		s1[cards[ch]] += 1
	for ch in seq[1]:
		s2[cards[ch]] += 1
	for ch in seq[2]:
		s3[cards[ch]] += 1
	for ch in seq[3]:
		if ch != '\n':
			s4[cards[ch]] += 1
	hands.append(s1 + s2 + s3 + s4)


X=pd.DataFrame(hands)
for i in range(0,4):
	X[13*(i)]*=5
	X[13*(i+1)-3]*=2
	X[13*(i+1)-2]*=3
	X[13*(i+1)-1]*=4


file.close()

file1 = open("a3y.csv", 'r')
output = []

for line in file1.readlines():
	string = line[1:-2]
	output.append([int(s) for s in string.split(',')])
y=pd.DataFrame(output)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.01,train_size = 0.5, random_state = 0)


xgb1=xgb.XGBClassifier(n_estimators=200, learning_rate=0.1, gamma=0, subsample=0.75, colsample_bytree=1, max_depth=8)
xgb1.fit(X_train,y_train[0])
y_pred1 = xgb1.predict(X[:50])



xgb2=xgb.XGBClassifier(n_estimators=200, learning_rate=0.1, gamma=0, subsample=0.75, colsample_bytree=1, max_depth=8)
xgb2.fit(X_train,y_train[1])
y_pred2 = xgb2.predict(X[:50])


xgb3=xgb.XGBClassifier(n_estimators=200, learning_rate=0.1, gamma=0, subsample=0.75, colsample_bytree=1, max_depth=8)
xgb3.fit(X_train,y_train[2])
y_pred3 = xgb3.predict(X[:50])


xgb4=xgb.XGBClassifier(n_estimators=200, learning_rate=0.1, gamma=0, subsample=0.75, colsample_bytree=1, max_depth=8)
xgb4.fit(X_train,y_train[3])
y_pred4 = xgb4.predict(X[:50])


xgb5=xgb.XGBClassifier(n_estimators=200, learning_rate=0.1, gamma=0, subsample=0.75, colsample_bytree=1, max_depth=8)
xgb5.fit(X_train,y_train[4])
y_pred5 = xgb5.predict(X[:50])

z1=pd.DataFrame(y_pred1)
z2=pd.DataFrame(y_pred2)
z3=pd.DataFrame(y_pred3)
z4=pd.DataFrame(y_pred4)
z5=pd.DataFrame(y_pred5)

z=pd.concat([z1,z2,z3,z4,z5], axis=1)




print  z
