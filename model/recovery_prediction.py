import pandas as pd
from sklearn.linear_model import LogisticRegression

# Sample logistics disruption dataset (prototype)
data = pd.DataFrame({
    "delay_hours": [5, 12, 20],
    "severity_level": [1, 2, 3],
    "route_priority": [3, 2, 1],
    "recovered_on_time": [1, 0, 0]
})

# Features and target
X = data[["delay_hours", "severity_level", "route_priority"]]
y = data["recovered_on_time"]

# Train model
model = LogisticRegression()
model.fit(X, y)

print("Logistics recovery prediction prototype trained successfully")
