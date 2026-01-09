import pandas as pd
from sklearn.linear_model import LogisticRegression

# Sample dataset (prototype data)
data = pd.DataFrame({
    "age": [30, 45, 60],
    "severity": [1, 2, 3],
    "recovered": [1, 1, 0]
})

# Features and target
X = data[["age", "severity"]]
y = data["recovered"]

# Train model
model = LogisticRegression()
model.fit(X, y)

print("Prototype model trained successfully")
