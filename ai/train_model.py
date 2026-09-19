import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# --------------------------------
# 1. Load training data
# --------------------------------

data = pd.read_csv("ai/training_data.csv")

print("Training data loaded successfully!")
print(data.head())


# --------------------------------
# 2. Separate input and target
# --------------------------------

X = data.drop("career", axis=1)
y = data["career"]

print("\nInput features:")
print(X.columns.tolist())

print("\nTarget:")
print(y.name)


# --------------------------------
# 3. Split data into training/testing
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.33,
    random_state=42,
    stratify=y
)

print("\nTraining data size:", len(X_train))
print("Testing data size:", len(X_test))


# --------------------------------
# 4. Define categorical columns
# --------------------------------

categorical_features = [
    "interest",
    "work_type",
    "career_goal"
]


# --------------------------------
# 5. Create preprocessor
# --------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# --------------------------------
# 6. Preprocess training data
# --------------------------------

X_train_processed = preprocessor.fit_transform(X_train)

X_test_processed = preprocessor.transform(X_test)

print("\nData preprocessing completed!")

print("Processed training data shape:",
      X_train_processed.shape)

print("Processed testing data shape:",
      X_test_processed.shape)


# --------------------------------
# 7. Create AI model
# --------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# --------------------------------
# 8. Train the model
# --------------------------------

model.fit(X_train_processed, y_train)

print("\nModel training completed successfully!")


# --------------------------------
# 9. Test the model
# --------------------------------

y_pred = model.predict(X_test_processed)


# --------------------------------
# 10. Calculate accuracy
# --------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Evaluation")
print("----------------")
print("Accuracy:", accuracy * 100, "%")


# --------------------------------
# 11. Classification report
# --------------------------------

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))


# --------------------------------
# 12. Test one sample
# --------------------------------

sample_prediction = model.predict(
    X_train_processed[0:1]
)

print("Sample Predicted Career:")
print(sample_prediction[0])


# --------------------------------
# 13. Save model and preprocessor
# --------------------------------

joblib.dump(
    model,
    "ai/career_model.pkl"
)

joblib.dump(
    preprocessor,
    "ai/preprocessor.pkl"
)

print("\nModel and preprocessor saved successfully!")