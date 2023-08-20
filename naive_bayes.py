import numpy as np
import pandas as pd
import math
# Define a function to load the heart disease data from a CSV file
def load_data(filename):
    return pd.read_csv(filename)
# Define a function to split the data into training and test sets
def split_data(X, Y, test_size=0.2):
    n = len(X)
    n_test = int(n * test_size)
    n_train = n - n_test
    indices = np.random.permutation(n)
    X_train = X[indices[:n_train]]
    X_test = X[indices[n_train:]]
    Y_train = Y[indices[:n_train]]
    Y_test = Y[indices[n_train:]]
    return X_train, X_test, Y_train, Y_test
# Define a function to calculate the mean and standard deviation of a dataset
def summarize_data(X):
    summaries = []
    for i in range(X.shape[1]):
        mean = X[:,i].mean()
        std = X[:,i].std()
        summaries.append((mean, std))
    return summaries
# Define a function to summarize the data by class
def summarize_by_class(X, Y):
    separated = {}
    for i in range(len(Y)):
        if Y[i] not in separated:
            separated[Y[i]] = []
        separated[Y[i]].append(X[i])
    summaries = {}
    for class_value, instances in separated.items():
        summaries[class_value] = summarize_data(np.asarray(instances))
    return summaries
# Define a function to calculate the Gaussian probability density function
def gaussian_probability(x, mean, std):
    exponent = -((x - mean) ** 2) / (2 * std ** 2)
    return (1 / (std * math.sqrt(2 * math.pi))) * math.exp(exponent)
# Define a function to calculate the class probabilities for a given row
def calculate_class_probabilities(summaries, row):
    probabilities = {}
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = 1
        for i in range(len(class_summaries)):
            mean, std = class_summaries[i]
            x = row[i]
            probabilities[class_value] *= gaussian_probability(x, mean, std)
    return probabilities
# Define a function to make a prediction for a given row
def predict(summaries, row):
    probabilities = calculate_class_probabilities(summaries, row)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label
# Define a function to make predictions for a test dataset
def get_predictions(summaries, X_test):
    predictions = []
    for i in range(len(X_test)):
        result = predict(summaries, X_test[i])
        predictions.append(result)
    return predictions
# Define a function to calculate the accuracy of the model
def calculate_accuracy(Y_test, predictions):
    correct = 0
    for i in range(len(Y_test)):
        if Y_test[i] == predictions[i]:
            correct += 1
    return (correct / float(len(Y_test))) 
# Load the heart disease data
dataset = load_data("C:\\Users\\rewan ahmed\\project (1)\\final_project\\heart.csv")
# Split the data into features and target
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values
# Split the data into training and test sets
X_train, X_test, Y_train, Y_test = split_data(X, Y, test_size=0.2)
# Summarize the training data by class
summaries = summarize_by_class(X_train, Y_train)
# Make predictions for the test data
predictions = get_predictions(summaries, X_test)
# Calculate the accuracy of the model
accuracy = calculate_accuracy(Y_test, predictions)
print('Accuracy: %.2f%%' % accuracy)
# Make a prediction for new data
input_data = np.asarray([58,1,0,114,318,0,2,140,0,4.4,0,3,1])
prediction = predict(summaries, input_data)
if prediction == 1:
    print('The person has heart disease')
else:
    print('The person does not have heart disease')

import matplotlib.pyplot as plt
plt.scatter(x=dataset.age[dataset.target==1], y=dataset.thalach[(dataset.target==1)], c="pink")
plt.scatter(x=dataset.age[dataset.target==0], y=dataset.thalach[(dataset.target==0)])
plt.legend(["Disease", "Not Disease"])
plt.xlabel("Age")
plt.ylabel("Maximum Heart Rate")
plt.text(80,100,'Team:\n\n1-Rewan ahmed ali\n2-sara abdelkader\n3-maryam jamal\n4-aya sabry\n5-alaa atef\n6-yasmeena ehab',
         fontsize=20,color='#000E8C', style='oblique',bbox = dict(facecolor = '#6A698C'))
plt.show()




