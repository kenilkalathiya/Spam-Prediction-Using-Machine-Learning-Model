import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle as pck
import os

# Read the data
base_dir = os.getcwd()
first = pd.read_csv('./dataset/fake_or_real_news.csv')
second = pd.read_csv('./dataset/fake_news_manual.csv')

boom_live = pd.read_csv('./dataset/boomlive_fake.csv')
the_hindu_real = pd.read_csv('./dataset/the_hindu_real.csv')

df = pd.concat([first, second, boom_live, the_hindu_real])
df.head()




labels=df['label']
labels.head()


title = df['title']

from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer(ngram_range=(1,5))

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(title, labels, test_size=0.2, random_state=7)

training_data = count_vector.fit_transform(x_train)

testing_data = count_vector.transform(x_test)

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)


predictions = naive_bayes.predict(testing_data)
predictions


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
print('Accuracy score: ', format(accuracy_score(y_test, predictions)))
print('Precision score: ', format(precision_score(y_test, predictions, average="binary", pos_label="REAL")))
print('Recall score: ', format(recall_score(y_test, predictions, average="binary", pos_label="REAL")))
print('F1 score: ', format(f1_score(y_test, predictions, average="binary", pos_label="REAL")))



text = df['text']



from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer(ngram_range=(1,5))

# Seperate the data into traning and testing 
from sklearn.model_selection import train_test_split
x_train_text,x_test_text,y_train_text,y_test_text=train_test_split(text, labels, test_size=0.2, random_state=7)


# Fit the training data and then return the matrix
training_data_text = count_vector.fit_transform(x_train_text)

# Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
testing_data_text = count_vector.transform(x_test_text)

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data_text, y_train_text)
# pck.dump(naive_bayes, open('NB_Model.pkl','wb'))

# print(testing_data_text)
predictions_text = naive_bayes.predict(testing_data_text)
predictions_text


# model = pck.load(open('NB_Model.pkl','rb'))
# model.predict(testing_data_text)

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
print('Accuracy score: ', format(accuracy_score(y_test_text, predictions_text)))
print('Precision score: ', format(precision_score(y_test_text, predictions_text, average="binary", pos_label="REAL")))
print('Recall score: ', format(recall_score(y_test_text, predictions_text, average="binary", pos_label="REAL")))
print('F1 score: ', format(f1_score(y_test_text, predictions_text, average="binary", pos_label="REAL")))


# # Checking Confusion Matrix
from sklearn.datasets import make_classification
from sklearn.metrics import plot_confusion_matrix

# Confusion Matrix for title
tn, fp, fn, tp = confusion_matrix(y_test, predictions).ravel()
(tn, fp, fn, tp)

# Cofusion Matrix for text
tnt, fpt, fnt, tpt = confusion_matrix(y_test_text, predictions_text).ravel()
(tnt, fpt, fnt, tpt)


# # Making It generalized
title = df['title']
text = df['text']

# Instantiate the CountVectorizer method
from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer(ngram_range=(1,1))
count_vector_text = CountVectorizer(ngram_range=(1,1))

# Seperate the data into traning and testing 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(title, labels, test_size=0.2, random_state=7)
x_train_text,x_test_text,y_train_text,y_test_text=train_test_split(text, labels, test_size=0.2, random_state=7)

# Fit the training data and then return the matrix
training_data = count_vector.fit_transform(x_train)
training_data_text = count_vector_text.fit_transform(x_train_text)



def main_function(input_news):
    # input_news = """
    # modi is dead
    # """

    testing_data = count_vector.transform([input_news])
    testing_data_text = count_vector.transform([input_news])

    # Making the model and fit it
    from sklearn.naive_bayes import MultinomialNB
    naive_bayes = MultinomialNB()
    naive_bayes_text = MultinomialNB()

    # Fitting the model
    naive_bayes.fit(training_data, y_train)
    naive_bayes_text.fit(training_data_text, y_train_text)

    # Predicting
    predictions = naive_bayes.predict(testing_data)
    # print(predictions)
    predictions_text = naive_bayes.predict(testing_data_text)
    # print(predictions_text)

    return predictions, predictions_text

# print(main_function("modi is dead"))