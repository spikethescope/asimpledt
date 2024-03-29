# -*- coding: utf-8 -*-
"""IRIS Simple Decision Tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GPjHe-JStF7sWdMRkM4C6IgzuPJIkVex
"""

# Importing the required packages
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Importing the required packages
from sklearn import datasets

# Loading the iris dataset
iris = datasets.load_iris()

# Printing the description of the iris dataset
print(iris.DESCR)

# Splitting the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state= 123)

#print(X_train)
# Building the decision tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluating the model's performance
y_pred = model.predict(X_test)
print(y_pred)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# prompt: write a code to generate confusion matrix for this model

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

y_pred = model.predict(X_test)
print(y_pred)
print(type(y_pred))
####EVALUATION OF THE MODEL###########
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, f1_score, accuracy_score


f1_score = f1_score(y_test, y_pred, average = "weighted")
accuracy_score = accuracy_score(y_test, y_pred)
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

# Calculate other metrics such as precision, recall, and specificity
classification_report = classification_report(y_test, y_pred)
print(classification_report)

from sklearn.tree import export_text
import matplotlib.pyplot as plt

# Plot the decision tree
plt.figure(figsize=(12, 8))
from sklearn.tree import plot_tree
plot_tree(model, feature_names= ['Sepal Length', 'Sepal Width', 'Petal length', 'Petal Width'], class_names=['Setosa', 'Versicolor', 'Virginica'], filled=True, rounded=True)
plt.show()
