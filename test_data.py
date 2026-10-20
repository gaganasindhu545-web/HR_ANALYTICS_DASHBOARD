import pandas as pd

# Load dataset
df = pd.read_csv("data/HR_Analytics.csv")

# 1. Dataset shape
print("=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# 2. First 5 rows
print("\n" + "=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())


# 3. Column names
print("\n" + "=" * 50)
print("COLUMN NAMES")
print("=" * 50)

for i, column in enumerate(df.columns, 1):
    print(i, "-", column)


# 4. Data types
print("\n" + "=" * 50)
print("DATA TYPES")
print("=" * 50)
print(df.dtypes)


# 5. Missing values
print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())


# 6. Duplicate rows
print("\n" + "=" * 50)
print("DUPLICATE ROWS")
print("=" * 50)
print("Duplicates:", df.duplicated().sum())


# 7. Attrition count
print("\n" + "=" * 50)
print("ATTRITION COUNT")
print("=" * 50)
print(df["Attrition"].value_counts())


# 8. Attrition percentage
print("\n" + "=" * 50)
print("ATTRITION PERCENTAGE")
print("=" * 50)
print(df["Attrition"].value_counts(normalize=True) * 100)


# 9. Statistical summary
print("\n" + "=" * 50)
print("STATISTICAL SUMMARY")
print("=" * 50)
print(df.describe())