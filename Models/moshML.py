import pandas as pd
from color_printer import *

## Machine learning A to predict your music genre
#* Based your gender and age (and data ofcourse)

df_musicFile = pd.read_csv("../Resources/music.csv")
# print(df_musicFile.shape) # overall (records, columns)
# print(df_musicFile.describe()) # basic info (mean - average values)
# print(df_musicFile.values) # list of rows (every row is also a list)
printYellow("Overall .csv data:")
print(df_musicFile) # Print the csv

# region the music.csv
#     age  gender      genre
# 0    20       1     HipHop
# 1    23       1     HipHop
# 2    25       1     HipHop
# 3    26       1       Jazz
# 4    29       1       Jazz
# 5    30       1       Jazz
# 6    31       1  Classical
# 7    33       1  Classical
# 8    37       1  Classical
# 9    20       0      Dance
# 10   21       0      Dance
# 11   25       0      Dance
# 12   26       0   Acoustic
# 13   27       0   Acoustic
# 14   30       0   Acoustic
# 15   31       0  Classical
# 16   34       0  Classical
# 17   35       0  Classical
# endregion the music.csv

## Part 1 - Define the input and output

# Make an inputValues list by .drop the "genre" from df_musicFile
x_inputValues = df_musicFile.drop (columns=['genre'])
# print(x_inputValues)

# Make an outputValues list
y_outputValues = df_musicFile["genre"]
# print(y_outputValues)

from sklearn.model_selection import train_test_split
x_input_train, x_input_test,\
y_output_train, y_output_test = \
    train_test_split(x_inputValues, y_outputValues,
                 test_size=0.3) # 30% result data save for testing

## Part 2 - Train the model and .predict
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

# train the model by insert the input (x) and output (y)
model.fit(X=x_input_train, y=y_output_train)

# Ask the mode to make a 2 predictions
# by new insert new x_inputValues records
# printYellow("Testing values .csv x_input_test:")
# print(x_input_test)
predictions = model.predict(x_input_test) # 22yrs old Man & Woman
# predictions = model.predict([[22, 1], [22, 0]]) # 22yrs old Man & Woman
# print(predictions)
# >> ['HipHop' 'Dance']
#~ Great! the model made a predictions based data

## Part 3 - Measure accuracy
# pre-made: 20% of the csv data has been kept for testing (x_input_test, y_output_test)
from sklearn.metrics import accuracy_score
printYellow("Correct .csv y_output_test:")
print(y_output_test)
printYellow("predictions:")
print(*predictions, sep='\n')

# Check accuracy ratio: Correct output VS. predictions output
accuracy_score = accuracy_score(y_output_test, predictions)
print(accuracy_score*100, "%")

