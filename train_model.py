import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


# --------------------------------------------------
# FILE NAMES
# --------------------------------------------------

DATA_FILE = "traffic_data.csv"
MODEL_FILE = "traffic_model.pkl"


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

df = pd.read_csv(DATA_FILE)

print("\nDataset loaded successfully!")
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))


# --------------------------------------------------
# SEPARATE INPUT AND OUTPUT
# --------------------------------------------------

X = df.drop(columns=["congestion_level"])
y = df["congestion_level"]


# --------------------------------------------------
# CATEGORICAL AND NUMERICAL FEATURES
# --------------------------------------------------

categorical_features = [
    "day_type",
    "weather"
]

numerical_features = [
    column for column in X.columns
    if column not in categorical_features
]


# --------------------------------------------------
# PREPROCESSING
# --------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),

        (
            "numerical",
            "passthrough",
            numerical_features
        )
    ]
)


# --------------------------------------------------
# RANDOM FOREST MODEL
# --------------------------------------------------

random_forest = RandomForestClassifier(
    n_estimators=250,
    max_depth=12,
    random_state=42,
    class_weight="balanced"
)


# --------------------------------------------------
# COMPLETE ML PIPELINE
# --------------------------------------------------

model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),

        (
            "classifier",
            random_forest
        )
    ]
)


# --------------------------------------------------
# TRAIN TEST SPLIT
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining the Random Forest model...")


# --------------------------------------------------
# TRAIN MODEL
# --------------------------------------------------

model.fit(X_train, y_train)


print("Model training completed!")


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# ACCURACY
# --------------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\n----------------------------------")
print("MODEL PERFORMANCE")
print("----------------------------------")

print(
    f"Accuracy: {accuracy * 100:.2f}%"
)


# --------------------------------------------------
# CLASSIFICATION REPORT
# --------------------------------------------------

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred
    )
)


# --------------------------------------------------
# SAVE MODEL
# --------------------------------------------------

joblib.dump(
    model,
    MODEL_FILE
)

print("----------------------------------")
print(f"Model saved as: {MODEL_FILE}")
print("----------------------------------")