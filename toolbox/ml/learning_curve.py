""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression

data = load_digits()
#print data.DESCR
num_trials = 10
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))

count = 0

for train_sizes in train_percentages:
	trial_acc = []
	for i in range(0, num_trials): # do 10 trials for each percentage
		X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=train_sizes)
		model = LogisticRegression(C=10**-20)
		model.fit(X_train, y_train)
		#print "Train accuracy %f" %model.score(X_train,y_train)
		#print "Test accuracy %f" %model.score(X_test,y_test)
		trial_acc.append(model.score(X_test,y_test))
	test_accuracies[count] = sum(trial_acc)/len(trial_acc)
	count+=1


# train a model with training percentages between 5 and 90 (see train_percentages) and evaluate
# the resultant accuracy.
# You should repeat each training percentage num_trials times to smooth out variability
# for consistency with the previous example use model = LogisticRegression(C=10**-10) for your learner


fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()