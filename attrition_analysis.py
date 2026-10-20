import pandas as pd

# Load dataset
df = pd.read_csv("data/HR_Analytics.csv")


# ==========================================
# 1. OVERALL ATTRITION
# ==========================================

total_employees = len(df)
employees_left = len(df[df["Attrition"] == "Yes"])

attrition_rate = (employees_left / total_employees) * 100

print("=" * 60)
print("OVERALL ATTRITION")
print("=" * 60)

print("Total Employees:", total_employees)
print("Employees Left:", employees_left)
print("Employees Stayed:", total_employees - employees_left)
print("Overall Attrition Rate:", round(attrition_rate, 2), "%")


# ==========================================
# 2. ATTRITION BY DEPARTMENT
# ==========================================

print("\n" + "=" * 60)
print("ATTRITION RATE BY DEPARTMENT")
print("=" * 60)

department_analysis = pd.crosstab(
    df["Department"],
    df["Attrition"],
    normalize="index"
) * 100

print(department_analysis.round(2))


# ==========================================
# 3. ATTRITION BY JOB ROLE
# ==========================================

print("\n" + "=" * 60)
print("ATTRITION RATE BY JOB ROLE")
print("=" * 60)

jobrole_analysis = pd.crosstab(
    df["JobRole"],
    df["Attrition"],
    normalize="index"
) * 100

print(jobrole_analysis.round(2))


# ==========================================
# 4. ATTRITION BY OVERTIME
# ==========================================

print("\n" + "=" * 60)
print("ATTRITION RATE BY OVERTIME")
print("=" * 60)

overtime_analysis = pd.crosstab(
    df["OverTime"],
    df["Attrition"],
    normalize="index"
) * 100

print(overtime_analysis.round(2))


# ==========================================
# 5. ATTRITION BY JOB SATISFACTION
# ==========================================

print("\n" + "=" * 60)
print("ATTRITION RATE BY JOB SATISFACTION")
print("=" * 60)

satisfaction_analysis = pd.crosstab(
    df["JobSatisfaction"],
    df["Attrition"],
    normalize="index"
) * 100

print(satisfaction_analysis.round(2))


# ==========================================
# 6. ATTRITION BY WORK-LIFE BALANCE
# ==========================================

print("\n" + "=" * 60)
print("ATTRITION RATE BY WORK-LIFE BALANCE")
print("=" * 60)

worklife_analysis = pd.crosstab(
    df["WorkLifeBalance"],
    df["Attrition"],
    normalize="index"
) * 100

print(worklife_analysis.round(2))