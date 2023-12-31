import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn import preprocessing
import matplotlib.pyplot as plt



data = {'Refund':['Yes','No','No','Yes','No','No','Yes','No','No','No'],
        'Marital_Status':['Single', 'Married','Single', 'Married','Divorced','Married','Divorced','Single', 'Married','Single'],
        'Taxable_Income': [125,100,70,120,95,60,220,85,75,90],
        'Defaulter': ['No','No','No','No','Yes','No','No','Yes','No','Yes']}
df = pd.DataFrame(data)
print(df)

label_encoders = {}
for column in df.columns[0:2]:
  le = preprocessing.LabelEncoder()
  df[column] = le.fit_transform(df[column])
  label_encoders[column] = le

print(df)

X = df.drop(columns=['Defaulter'])
y = df['Defaulter']

model = DecisionTreeClassifier()
model.fit(X,y)


# Print the decision tree rules
tree_rules = export_text(model, feature_names=X.columns.tolist())
print("Decision Tree Rules:")
print(tree_rules)

# Plot the decision tree
plt.figure(figsize=(12, 8))
from sklearn.tree import plot_tree
plot_tree(model, feature_names=X.columns.tolist(), class_names=['Yes', 'No'], filled=True, rounded=True)
plt.show()
