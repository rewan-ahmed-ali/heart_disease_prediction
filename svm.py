import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# Loading the heart diseases  (csv) to a pandas DataFrame
Heart_Data = pd.read_csv("C:\\Users\\rewan ahmed\\project (1)\\final_project\\heart.csv")
# splitting the features and target
X = Heart_Data.drop(columns='target' , axis=1)
Y = Heart_Data['target']
# splitting the data into the training data & test data
X_train , X_test , Y_train , Y_test = train_test_split(X , Y ,test_size= 0.2 , stratify= Y ,random_state=42)
# طبع عدد الاعمدة والصفوف
# print(X.shape , X_train.shape , X_test.shape)
# SVM
svm = SVC(kernel="linear", C=1.0, gamma="auto")
svm.fit(X_train, Y_train)
# accuracy on training data
X_train_Prediction = svm.predict(X_train)
trainig_data_accuracy = accuracy_score(X_train_Prediction , Y_train )
print("Accuracy on training data : " , trainig_data_accuracy)
# accuracy on test data
X_test_Prediction =svm.predict(X_test)
test_data_accuracy = accuracy_score(X_test_Prediction , Y_test )
print("Accuracy on test data : " , test_data_accuracy)
# Building a predictive system
input_data = (66,1,0,112,212,0,0,132,1,0.1,2,1,2)
# change the input_data to a numpu array
input_data_as_numpy_array = np.asarray(input_data)
# reshape the numpy array as we are predicting for only on instance 
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = svm.predict(input_data_reshaped)
print(prediction)
if prediction[0] == 1 :
    print("the person has heart disease")
else :
    print("the person not has heart disease") 

