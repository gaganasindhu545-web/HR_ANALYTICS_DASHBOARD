import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/HR_Analytics.csv")

# Set visualization style
sns.set_theme(style="whitegrid")


# ==========================================
# 1. ATTRITION DISTRIBUTION
# ==========================================

plt.figure(figsize=(6, 5))

sns.countplot(data=df, x="Attrition")

plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

plt.show()


# ==========================================
# 2. ATTRITION BY DEPARTMENT
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="Department", hue="Attrition")

plt.title("Employee Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.xticks(rotation=15)

plt.show()


# ==========================================
# 3. ATTRITION BY JOB ROLE
# ==========================================

plt.figure(figsize=(10, 6))

sns.countplot(data=df, y="JobRole", hue="Attrition")

plt.title("Employee Attrition by Job Role")
plt.xlabel("Number of Employees")
plt.ylabel("Job Role")

plt.show()


# ==========================================
# 4. ATTRITION VS OVERTIME
# ==========================================

plt.figure(figsize=(7, 5))

sns.countplot(data=df, x="OverTime", hue="Attrition")

plt.title("Overtime vs Employee Attrition")
plt.xlabel("Overtime")
plt.ylabel("Number of Employees")

plt.show()


# ==========================================
# 5. JOB SATISFACTION VS ATTRITION
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="JobSatisfaction", hue="Attrition")

plt.title("Job Satisfaction vs Employee Attrition")
plt.xlabel("Job Satisfaction")
plt.ylabel("Number of Employees")

plt.show()


# ==========================================
# 6. AGE VS ATTRITION
# ==========================================

plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="Attrition", y="Age")

plt.title("Age vs Employee Attrition")
plt.xlabel("Attrition")
plt.ylabel("Age")

plt.show()


# ==========================================
# 7. MONTHLY INCOME VS ATTRITION
# ==========================================

plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="Attrition", y="MonthlyIncome")

plt.title("Monthly Income vs Employee Attrition")
plt.xlabel("Attrition")
plt.ylabel("Monthly Income")

plt.show()


# ==========================================
# 8. WORK-LIFE BALANCE VS ATTRITION
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="WorkLifeBalance", hue="Attrition")

plt.title("Work-Life Balance vs Employee Attrition")
plt.xlabel("Work-Life Balance")
plt.ylabel("Number of Employees")

plt.show()