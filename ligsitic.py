import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# Loading the heart diseases  (csv) to a pandas DataFrame
Heart_Data = pd.read_csv("C:\\Users\\rewan ahmed\\project (1)\\final_project\\heart.csv")
# splitting the features and target
X = Heart_Data.drop(columns='target' , axis=1)
Y = Heart_Data['target']
# print(X)
# print(Y)
# splitting the data into the training data & test data
X_train , X_test , Y_train , Y_test = train_test_split(X , Y ,test_size= 0.2 , random_state=2 )
# طبع عدد الاعمدة والصفوف
# print(X.shape , X_train.shape , X_test.shape)
# model training 
# Logistic Regression
model = LogisticRegression()
# training the LogisticRegressio model with training data
model.fit(X_train ,Y_train)
# Model Evaluation 
# accuracy on training data
X_train_Prediction = model.predict(X_train)
trainig_data_accuracy = accuracy_score(X_train_Prediction , Y_train )
print("Accuracy on training data : " , trainig_data_accuracy)
# accuracy on test data
X_test_Prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_Prediction , Y_test )
print("Accuracy on test data : " , test_data_accuracy)
# Building a predictive system
input_data = (52,1,0,125,212,0,1,168,0,1,2,2,3)
# change the input_data to a numpu array
input_data_as_numpy_array = np.asarray(input_data)
# reshape the numpy array as we are predicting for only on instance 
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)
if prediction[0] == 1 :
    print("the person has heart disease")
else :
    print("the person not has heart disease") 
import matplotlib.pyplot as plt
plt.scatter(x=Heart_Data.age[Heart_Data.target==1], y=Heart_Data.thalach[(Heart_Data.target==1)], c="pink")
plt.scatter(x=Heart_Data.age[Heart_Data.target==0], y=Heart_Data.thalach[(Heart_Data.target==0)])
plt.legend(["Disease", "Not Disease"])
plt.xlabel("Age")
plt.ylabel("Maximum Heart Rate")
plt.text(80,100,'Team:\n\n1-Rewan ahmed ali\n2-sara abdelkader\n3-maryam jamal\n4-aya sabry\n5-alaa atef\n6-yasmeena ehab',
         fontsize=20,color='#000E8C', style='oblique',bbox = dict(facecolor = '#6A698C'))
plt.show()








