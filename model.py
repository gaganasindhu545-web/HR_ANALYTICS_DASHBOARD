import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# ==========================================================
# 1. LOAD DATA
# ==========================================================

df = pd.read_csv("data/HR_Analytics.csv")

print("=" * 60)
print("DATASET LOADED")
print("=" * 60)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ==========================================================
# 2. REMOVE UNNECESSARY COLUMNS
# ==========================================================

columns_to_remove = [
    "EmployeeCount",
    "EmployeeNumber",
    "Over18",
    "StandardHours"
]

df = df.drop(columns=columns_to_remove)


# ==========================================================
# 3. FEATURES AND TARGET
# ==========================================================

X = df.drop("Attrition", axis=1)

y = df["Attrition"].map({
    "No": 0,
    "Yes": 1
})


# ==========================================================
# 4. IDENTIFY COLUMN TYPES
# ==========================================================

categorical_columns = X.select_dtypes(
    include=["object", "string"]
).columns.tolist()

numeric_columns = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()


print("\nCategorical Columns:")
print(categorical_columns)

print("\nNumeric Columns:")
print(numeric_columns)


# ==========================================================
# 5. PREPROCESSING
# ==========================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        ),

        (
            "numeric",
            StandardScaler(),
            numeric_columns
        )
    ]
)


# ==========================================================
# 6. TRAIN TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================================
# 7. MODELS
# ==========================================================

models = {

    "Logistic Regression": LogisticRegression(
        max_iter=3000,
        class_weight="balanced"
    ),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42,
        class_weight="balanced",
        max_depth=6
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        class_weight="balanced",
        max_depth=10
    )
}


# ==========================================================
# 8. TRAIN AND EVALUATE
# ==========================================================

results = {}

best_model = None
best_f1 = 0
best_model_name = ""


for name, model in models.items():

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    # Train
    pipeline.fit(X_train, y_train)

    # Prediction
    y_pred = pipeline.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_pred,
        zero_division=0
    )

    results[name] = [
        accuracy,
        precision,
        recall,
        f1
    ]

    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1 Score :", round(f1, 4))

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            y_pred,
            target_names=[
                "No Attrition",
                "Attrition"
            ],
            zero_division=0
        )
    )

    print("Confusion Matrix:")

    print(
        confusion_matrix(
            y_test,
            y_pred
        )
    )

    # Select best model using F1 score
    if f1 > best_f1:

        best_f1 = f1
        best_model = pipeline
        best_model_name = name


# ==========================================================
# 9. MODEL COMPARISON
# ==========================================================

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

results_df = pd.DataFrame(
    results,
    index=[
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
).T

print(results_df.round(4))


# ==========================================================
# 10. SAVE BEST MODEL
# ==========================================================

model_path = "models/attrition_model.pkl"

joblib.dump(
    best_model,
    model_path
)


print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print("Model:", best_model_name)
print("F1 Score:", round(best_f1, 4))

print("\nModel saved successfully!")
print("Location:", model_path)