# train_model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Generate synthetic data
np.random.seed(42)
n = 1000
data = {
    "WBC": np.random.normal(7, 2, n),
    "RBC": np.random.normal(5, 0.5, n),
    "Hemoglobin": np.random.normal(14, 1.5, n),
    "Platelets": np.random.normal(250, 75, n),
    "MCV": np.random.normal(90, 5, n),
    "Lymphocytes": np.random.normal(30, 10, n),
    "Neutrophils": np.random.normal(60, 10, n),
    "Diagnosis": np.random.choice(["Healthy", "Leukemia", "Lymphoma"], size=n, p=[0.5, 0.25, 0.25])
}
df = pd.DataFrame(data)

# Encode target
df["Diagnosis"] = df["Diagnosis"].astype("category").cat.codes  # 0: Healthy, 1: Leukemia, 2: Lymphoma

X = df.drop("Diagnosis", axis=1)
y = df["Diagnosis"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "cancer_model.pkl")