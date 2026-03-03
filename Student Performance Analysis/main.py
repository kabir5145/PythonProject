import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.ma.core import dot

# Load dataset
file = pd.read_csv("student_data.csv")
print(file.to_string())

# -------------------------------
# 1 Create Total and Average Marks
# -------------------------------
file["Total_Marks"] = file["Previous_Marks"] + file["Final_Marks"]
file["Average_Marks"] = file["Total_Marks"] / 2

# -------------------------------
# 2 Pass / Fail Logic
# -------------------------------
pass_marks = 80
file["Result"] = np.where(file["Total_Marks"] >= pass_marks, "Pass", "Fail")

# -------------------------------
# 3 Grade System
# -------------------------------
conditions = [
    file["Average_Marks"] >= 90,
    file["Average_Marks"] >= 75,
    file["Average_Marks"] >= 60,
    file["Average_Marks"] >= 50
]

grades = ["A", "B", "C", "D"]

file["Grade"] = np.select(conditions, grades, default="F")

# -------------------------------
# 4 Statistics
# -------------------------------
highest_score = file["Total_Marks"].max()
lowest_score = file["Total_Marks"].min()
mean_score = file["Total_Marks"].mean()

print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Average Score:", mean_score)

# -------------------------------
# 5 Normalization (ML Concept)
# -------------------------------
normalized = (file["Total_Marks"] - file["Total_Marks"].min()) / \
             (file["Total_Marks"].max() - file["Total_Marks"].min())

file["Normalized_Score"] = normalized

print("Statistical Summary of Dataset:")
print(file.describe())

# -------------------------------
# 6 Visualization
# -------------------------------
plt.figure(figsize=(12,8))

#  Bar Chart – Grade Distribution
plt.subplot(2,2,1)
file["Grade"].value_counts().plot(kind="bar",color="yellow",edgecolor="black")
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")

#  Histogram – Total Marks Distribution
plt.subplot(2,2,2)
plt.hist(file["Total_Marks"], bins=5,color="green",edgecolor="black")
plt.title("Total Marks Distribution")
plt.xlabel("Total Marks")
plt.ylabel("Frequency")

# Pie Chart – Pass vs Fail
plt.subplot(2,2,3)
file["Result"].value_counts().plot(kind="pie", autopct="%1.1f%%",colors="red",)
plt.title("Pass vs Fail")

#  Line Plot – Average Marks Trend
plt.subplot(2,2,4)
plt.plot(file["Average_Marks"])
plt.title("Average Marks Trend")

plt.tight_layout()
plt.show()

