
import numpy as np
import pandas as pd
import joblib 
import sys
#inputfile = pd.read_csv('input.txt' , header=None)
#X= inputfile.iloc[:, 0:91]
file = sys.stdin
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
	X[13*(i)]*=10
	X[13*(i+1)-3]*=4
	X[13*(i+1)-2]*=6
	X[13*(i+1)-1]*=8


file.close()


taramodel = joblib.load("OVR2x.txt")
y_pred = taramodel.predict(X)

for line in y_pred:
	string = ''
	for ch in line:
		string += str(ch) + ','
	print string[:-1]

#z=pd.DataFrame(y_pred)
#z=z.round(0).astype(int)
#print (z.to_string(index = False, header=False))