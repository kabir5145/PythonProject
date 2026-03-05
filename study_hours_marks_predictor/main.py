import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = {
    "Hours":[1,2,3,4,5],
    "Marks":[2,4,5,4,5]
}

df = pd.DataFrame(data)

x = df["Hours"]
y = df["Marks"]

n = len(x)

# calculate slope (m)
m = (n*np.sum(x*y) - np.sum(x)*np.sum(y)) / (n*np.sum(x**2) - (np.sum(x))**2)

# calculate intercept (c)
c = (np.sum(y) - m*np.sum(x)) / n

print("m =", m)
print("c =", c)

# predicted line
y_predict = m*x + c

# predict marks for new hours
new_hours = 6
predicted_marks = m * new_hours + c

print("Predicted marks for", new_hours, "hours:", predicted_marks)

# plot
plt.scatter(x,y,label="Actual Data")
plt.plot(x,y_predict,color="red",label="y = mx + c")

plt.xlabel("Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()

