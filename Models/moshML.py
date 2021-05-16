import pandas as pd

## Machine learning A to predict your music genre
#* Based your gender and age (and data ofcourse)

df_musicFile = pd.read_csv("../Resources/music.csv")
# print(df_musicFile.shape) # overall (records, columns)
# print(df_musicFile.describe()) # basic info (mean - average values)
# print(df_musicFile.values) # list of rows (every row is also a list)
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

## Part 2 - Train the model and .predict
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

# train the model by insert the input (x) and output (y)
model.fit(X=x_inputValues, y=y_outputValues)

# Ask the mode to make a 2 predictions
# by new insert new x_inputValues records
predictions = model.predict([[22, 1], [22, 0]]) # 22yrs old Man & Woman
print(predictions)
# >> ['HipHop' 'Dance']
#~ Great! the model made a predictions based data
