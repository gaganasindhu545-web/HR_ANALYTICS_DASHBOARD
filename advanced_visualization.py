import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/HR_Analytics.csv")

sns.set_theme(style="whitegrid")


# ==========================================================
# 1. OVERALL ATTRITION - PIE CHART
# ==========================================================

attrition_counts = df["Attrition"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    attrition_counts,
    labels=attrition_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Overall Employee Attrition")
plt.tight_layout()
plt.show()


# ==========================================================
# 2. ATTRITION RATE BY DEPARTMENT
# ==========================================================

department_rate = (
    df.groupby("Department")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=department_rate.index,
    y=department_rate.values
)

plt.title("Attrition Rate by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")

for i, value in enumerate(department_rate.values):
    plt.text(i, value + 0.5, f"{value:.1f}%", ha="center")

plt.tight_layout()
plt.show()


# ==========================================================
# 3. ATTRITION RATE BY JOB ROLE
# ==========================================================

jobrole_rate = (
    df.groupby("JobRole")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=True)
)

plt.figure(figsize=(10, 7))

sns.barplot(
    x=jobrole_rate.values,
    y=jobrole_rate.index
)

plt.title("Attrition Rate by Job Role")
plt.xlabel("Attrition Rate (%)")
plt.ylabel("Job Role")

for i, value in enumerate(jobrole_rate.values):
    plt.text(value + 0.5, i, f"{value:.1f}%", va="center")

plt.tight_layout()
plt.show()


# ==========================================================
# 4. ATTRITION RATE BY OVERTIME
# ==========================================================

overtime_rate = (
    df.groupby("OverTime")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

plt.figure(figsize=(7, 5))

sns.barplot(
    x=overtime_rate.index,
    y=overtime_rate.values
)

plt.title("Attrition Rate by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")

for i, value in enumerate(overtime_rate.values):
    plt.text(i, value + 0.5, f"{value:.1f}%", ha="center")

plt.tight_layout()
plt.show()


# ==========================================================
# 5. JOB SATISFACTION VS ATTRITION
# ==========================================================

satisfaction_rate = (
    df.groupby("JobSatisfaction")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=satisfaction_rate.index,
    y=satisfaction_rate.values
)

plt.title("Attrition Rate by Job Satisfaction")
plt.xlabel("Job Satisfaction Level")
plt.ylabel("Attrition Rate (%)")

for i, value in enumerate(satisfaction_rate.values):
    plt.text(i, value + 0.5, f"{value:.1f}%", ha="center")

plt.tight_layout()
plt.show()


# ==========================================================
# 6. WORK-LIFE BALANCE VS ATTRITION
# ==========================================================

worklife_rate = (
    df.groupby("WorkLifeBalance")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=worklife_rate.index,
    y=worklife_rate.values
)

plt.title("Attrition Rate by Work-Life Balance")
plt.xlabel("Work-Life Balance Level")
plt.ylabel("Attrition Rate (%)")

for i, value in enumerate(worklife_rate.values):
    plt.text(i, value + 0.5, f"{value:.1f}%", ha="center")

plt.tight_layout()
plt.show()


# ==========================================================
# 7. AGE DISTRIBUTION BY ATTRITION
# ==========================================================

plt.figure(figsize=(9, 5))

sns.histplot(
    data=df,
    x="Age",
    hue="Attrition",
    kde=True,
    bins=20
)

plt.title("Age Distribution by Employee Attrition")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.show()


# ==========================================================
# 8. MONTHLY INCOME VS ATTRITION
# ==========================================================

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Attrition",
    y="MonthlyIncome"
)

plt.title("Monthly Income vs Employee Attrition")
plt.xlabel("Attrition")
plt.ylabel("Monthly Income")

plt.tight_layout()
plt.show()


print("\nAll advanced visualizations completed successfully!")