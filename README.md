# ⚽ FIFA World Cup Match Prediction

A Machine Learning project that predicts football match outcomes using historical international football data.

## 🛠 Technologies Used
- Python
- Pandas
- Scikit-Learn
- Random Forest Classifier

## 📊 Workflow
1. Load and preprocess data
2. Encode team names using LabelEncoder
3. Split data into training and testing sets
4. Train a Random Forest model
5. Evaluate performance using Accuracy Score

## 📈 Result
The model predicts match winners based on historical match data.

## 🚀 Libraries Used

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
