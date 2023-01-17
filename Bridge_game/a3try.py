import numpy as np
import pandas as pd
import sklearn
import sklearn.multiclass as skm
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
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
#print X


file.close()

file1 = open("a3y.csv", 'r')
output = []

for line in file1.readlines():
	string = line[1:-2]
	output.append([int(s) for s in string.split(',')])
y=pd.DataFrame(output)
#print y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.0001,train_size=0.9, random_state = 0)
td=skm.OneVsRestClassifier(LinearSVC(random_state=0)).fit(X_train, y_train)
ypred = td.predict(X[:50])
z=pd.DataFrame(ypred)
print z
joblib.dump(td,"OVRcoff.txt")
#test=pd.DataFrame(y_test)
#print test