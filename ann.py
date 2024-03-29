#   Artificial neural Network
#   Part 1-Preprocessing
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values
# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
#   creating dummy variables for countries
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:,1:]


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#   Part-2 Building ANN
import keras
from keras.models import Sequential
from keras.layers import Dense 
classifier =Sequential()

#first hidden layer and input layer
classifier.add(Dense(6, kernel_initializer='uniform', activation = 'relu', input_shape=(11,)))
#second hidden layer 
classifier.add(Dense(6, kernel_initializer='uniform', activation = 'relu'))

# o/p layer

classifier.add(Dense(1, kernel_initializer='uniform', activation = 'sigmoid'))

# compiling the ANN
classifier.compile(optimizer= 'adam' , loss= 'binary_crossentropy' ,metrics =['accuracy'] )


# fitting the ANN to the training set
classifier.fit(X_train, y_train ,batch_size = 5, epochs=110)
# Part-3 make prediction
# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred= (y_pred > 0.5)




# predicting for a signle test


new_prediction= classifier.predict(sc.transform(np.array([[0.0,0,120,1,20,3,6000,2,1,1,500]]))) # row is required
new_prediction= (new_prediction > .5)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)