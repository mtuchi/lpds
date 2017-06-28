# Gender Classfier
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

#[height, weight]
dflog = pd.read_csv("dataset/01_heights_weights_genders.csv")
dflog.head(10)

# Split the data into a training and test set.
Xlr, Xtestlr, ylr, ytestlr = train_test_split(dflog[['Height','Weight']].values,
                                              (dflog.Gender).values,random_state=5)

# clf = LogisticRegression()
clf = tree.DecisionTreeClassifier()
# Fit the model on the trainng data.
clf.fit(Xlr, ylr)

predection = clf.predict([68.8976, 130.073])
print predection
# print(Xlr)
# print(ylr)
# print(Xtestlr)
# print(ytestlr)

# Print the accuracy from the testing data.
print(accuracy_score(clf.predict(Xlr), ylr))
