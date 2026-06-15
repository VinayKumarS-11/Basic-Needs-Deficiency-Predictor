import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("readyy.csv")

# Create score
df["Basic_Needs_Score"] = (
    df["Water"] +
    df["Sanitation"] +
    df["Electricity"] +
    df["Education"] +
    df["Nutrition"]
) / 5

# Create labels
def classify(score):
    if score >= 75:
        return "Efficient"
    elif score >= 50:
        return "Moderate"
    else:
        return "Deficient"

df["Status"] = df["Basic_Needs_Score"].apply(classify)

# Features
X = df[[
    "Water",
    "Sanitation",
    "Electricity",
    "Education",
    "Nutrition"
]]

# Target
y = df["Status"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model Saved Successfully")