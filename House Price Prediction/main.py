import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('Housing.csv')

#--------------------------
# 1.Load and Explore Data
#--------------------------

print(df.head().to_string())
print(df.shape)
print(df.describe())

#--------------------------
# 2.Prepare Features and Labels
#--------------------------

# Convert categorical data
df = pd.get_dummies(df, drop_first=True)

# Features and labels
X = df.drop("price", axis=1)
y = df["price"]

#--------------------------
# 3.Split Training and Testing Data
#--------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

#--------------------------
# 4.Train the Machine Learning Model
#--------------------------

regressor = LinearRegression()
regressor.fit(X_train, y_train)

#-------------------------
# 5.Make Predictions
#-------------------------

y_prediction = regressor.predict(X_test)
print("Predicted Price: ", y_prediction)
print("Actual Price: ", y_test)
print("Model Score:", r2_score(y_test, y_prediction))

#-------------------------
# 6. Predict New House Price
#-------------------------

new_house = [X.iloc[0].values]

predicted_price = regressor.predict(new_house)

print("Predicted Price:", predicted_price[0])
print("Actual Price:", y_test.iloc[0])

#-------------------------
# 7.Visualize Results
#-------------------------

plt.scatter(df['price'], df['area'])
plt.xlabel('House Price')
plt.ylabel('Area')
plt.show()

