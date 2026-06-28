import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Dataset
print("Loading Dataset...")

df = pd.read_csv("dataset.csv")

print("\nDataset Loaded Successfully")
print("Shape:", df.shape)

# Remove index column
if "index" in df.columns:
    df = df.drop("index", axis=1)

# Features and Target
X = df.drop("Result", axis=1)
y = df["Result"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest Model
print("\nTraining Model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model Training Completed")

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Sample Prediction
sample = X.iloc[[0]]

prediction = model.predict(sample)

print("\nSample Prediction:")

if prediction[0] == 1:
    print("Legitimate Website")
elif prediction[0] == 0:
    print("Suspicious Website")
else:
    print("Phishing Website")

import joblib

joblib.dump(model, "phishing_model.pkl")

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
})

print(feature_importance.sort_values(
    by='Importance',
    ascending=False
).head(10))
prediction = model.predict(sample)
print(prediction)
print(df["Result"].value_counts())