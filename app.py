
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="HR Analytics & Attrition Prediction",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ===== GLOBAL ===== */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f8f7ff 0%, #f4f8ff 48%, #f8fbff 100%);
}

.block-container {
    padding-top: .75rem;
    padding-bottom: 1.2rem;
    max-width: 1350px;
}

/* colorful top accent */
.block-container:before {
    content: '';
    display: block;
    height: 5px;
    border-radius: 8px;
    margin-bottom: 14px;
    background: linear-gradient(90deg, #6d28d9, #4f46e5, #0891b2, #10b981, #f59e0b);
}

/* ===== MAIN TITLE ===== */
.main-title {
    font-size: 30px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #312e81, #6d28d9, #0f766e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
    letter-spacing: -1px;
}

.subtitle {
    text-align: center;
    font-size: 11px;
    color: #64748b;
    margin-bottom: 18px;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #15132b 0%, #25205b 100%);
    border-right: none;
}

section[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

section[data-testid="stSidebar"] .stRadio > label {
    font-weight: 700;
    font-size: 12px;
    letter-spacing: .5px;
}

section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
    gap: 6px;
}

section[data-testid="stSidebar"] .stRadio label {
    padding: 8px 9px;
    border-radius: 10px;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,.09);
}

section[data-testid="stSidebar"] .stAlert {
    background: rgba(255,255,255,.09);
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 12px;
}

/* ===== METRIC CARDS ===== */
div[data-testid="stMetric"] {
    background: rgba(255,255,255,.96);
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 8px 12px;
    box-shadow: 0 7px 20px rgba(30,41,59,.07);
    min-height: 70px;
    position: relative;
    overflow: hidden;
    transition: transform .2s ease, box-shadow .2s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(30,41,59,.11);
}

div[data-testid="stMetric"]:after {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 4px;
    background: linear-gradient(180deg, #7c3aed, #4f46e5);
}

div[data-testid="stHorizontalBlock"] > div:nth-child(2) div[data-testid="stMetric"]:after { background: linear-gradient(180deg,#f97316,#ef4444); }
div[data-testid="stHorizontalBlock"] > div:nth-child(3) div[data-testid="stMetric"]:after { background: linear-gradient(180deg,#10b981,#059669); }
div[data-testid="stHorizontalBlock"] > div:nth-child(4) div[data-testid="stMetric"]:after { background: linear-gradient(180deg,#06b6d4,#2563eb); }

div[data-testid="stMetric"] label {
    color: #64748b !important;
    font-weight: 600;
    font-size: 11px;
}

div[data-testid="stMetricValue"] {
    color: #111827;
    font-weight: 800;
    font-size: 22px;
}

/* ===== HEADINGS ===== */
h1, h2, h3 {
    color: #172033;
    letter-spacing: -.3px;
}

.stSubheader {
    color: #312e81 !important;
    font-weight: 800 !important;
}

/* filter controls */
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,.95) !important;
    border: 1px solid #d9d6fe !important;
    box-shadow: 0 3px 10px rgba(79,70,229,.06);
}

/* colorful sidebar title */
section[data-testid="stSidebar"] h1 {
    background: linear-gradient(90deg,#c4b5fd,#67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

[data-testid="stHeader"] {
    background: transparent;
}

/* ===== CONTENT CONTAINERS ===== */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 12px;
}

/* ===== DATAFRAME ===== */
div[data-testid="stDataFrame"] {
    border: 1px solid #e6eaf0;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(15,23,42,.04);
}

/* ===== INPUTS ===== */
div[data-baseweb="select"] > div,
input,
textarea {
    border-radius: 10px !important;
}

/* ===== BUTTON ===== */
.stButton > button {
    border: none;
    border-radius: 11px;
    background: linear-gradient(135deg, #5146e5, #7c3aed);
    color: white;
    font-weight: 700;
    min-height: 38px;
    box-shadow: 0 7px 18px rgba(79,70,229,.20);
}

.stButton > button:hover {
    color: white;
    background: linear-gradient(135deg, #4338ca, #6d28d9);
}

/* ===== ALERTS ===== */
div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* ===== DIVIDERS ===== */
hr {
    border-color: #e5e7eb;
}

/* ===== FOOTER ===== */
footer {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

@media (max-width: 900px) {
    .main-title {
        font-size: 30px;
    }
    .subtitle {
        font-size: 14px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():
    return pd.read_csv("data/HR_Analytics.csv")


@st.cache_resource
def load_model():
    return joblib.load("models/attrition_model.pkl")


df = load_data()
model = load_model()


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("👥 HR Analytics")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📊 HR Analytics",
        "💡 Attrition Insights",
        "👤 Employee Risk & Performance",
        "🤖 Attrition Prediction",
        "📈 Model Performance"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "HR Analytics & Employee Attrition "
    "Prediction System"
)


# ==========================================================
# DASHBOARD
# ==========================================================

if page == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">HR Analytics & Employee Attrition</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Interactive workforce intelligence dashboard</div>',
        unsafe_allow_html=True
    )

    # ------------------------------------------------------
    # INTERACTIVE DASHBOARD FILTERS
    # ------------------------------------------------------
    f1, f2, f3, f4 = st.columns(4)

    with f1:
        dashboard_department = st.selectbox(
            "🏢 Department",
            ["All"] + sorted(df["Department"].unique()),
            key="dashboard_department"
        )

    with f2:
        dashboard_overtime = st.selectbox(
            "⏰ Overtime",
            ["All"] + sorted(df["OverTime"].unique()),
            key="dashboard_overtime"
        )

    with f3:
        dashboard_gender = st.selectbox(
            "👤 Gender",
            ["All"] + sorted(df["Gender"].unique()),
            key="dashboard_gender"
        )

    with f4:
        dashboard_attrition = st.selectbox(
            "📉 Attrition",
            ["All", "Yes", "No"],
            key="dashboard_attrition"
        )

    filtered_dashboard = df.copy()

    if dashboard_department != "All":
        filtered_dashboard = filtered_dashboard[
            filtered_dashboard["Department"] == dashboard_department
        ]

    if dashboard_overtime != "All":
        filtered_dashboard = filtered_dashboard[
            filtered_dashboard["OverTime"] == dashboard_overtime
        ]

    if dashboard_gender != "All":
        filtered_dashboard = filtered_dashboard[
            filtered_dashboard["Gender"] == dashboard_gender
        ]

    if dashboard_attrition != "All":
        filtered_dashboard = filtered_dashboard[
            filtered_dashboard["Attrition"] == dashboard_attrition
        ]

    total_employees = len(filtered_dashboard)
    employees_left = len(
        filtered_dashboard[filtered_dashboard["Attrition"] == "Yes"]
    )
    employees_stayed = len(
        filtered_dashboard[filtered_dashboard["Attrition"] == "No"]
    )

    attrition_rate = (
        (employees_left / total_employees) * 100
        if total_employees > 0 else 0
    )

    # ------------------------------------------------------
    # COMPACT KPI CARDS
    # ------------------------------------------------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Total Employees", f"{total_employees:,}")
    col2.metric("🚪 Employees Left", f"{employees_left:,}")
    col3.metric("✅ Employees Stayed", f"{employees_stayed:,}")
    col4.metric("📉 Attrition Rate", f"{attrition_rate:.2f}%")

    if total_employees == 0:
        st.warning("No employees match the selected dashboard filters.")
    else:

        st.markdown("---")

        # --------------------------------------------------
        # SMALLER INTERACTIVE CHARTS
        # --------------------------------------------------
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🍩 Attrition Distribution")

            attrition_counts = filtered_dashboard["Attrition"].value_counts()

            fig, ax = plt.subplots(figsize=(4.0, 2.65))
            fig.patch.set_alpha(0)
            ax.set_facecolor("#ffffff")
            pie_colors = ["#6366f1", "#f97316"]
            wedges, texts, autotexts = ax.pie(
                attrition_counts.values,
                labels=attrition_counts.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=pie_colors[:len(attrition_counts)],
                pctdistance=.72,
                wedgeprops={"width":0.42, "edgecolor":"white", "linewidth":2},
                textprops={"fontsize": 8, "fontweight": "bold"}
            )
            for txt in autotexts:
                txt.set_color("#111827")
            ax.set_title("Employee Attrition", fontsize=10, fontweight="bold", color="#312e81", pad=5)
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        with col2:
            st.subheader("🏢 Department Attrition")

            department_rate = (
                filtered_dashboard.groupby("Department")["Attrition"]
                .apply(lambda x: (x == "Yes").mean() * 100)
                .sort_values(ascending=True)
            )

            fig, ax = plt.subplots(figsize=(5.0, 2.65))
            fig.patch.set_alpha(0)
            bars = ax.barh(department_rate.index, department_rate.values, color=["#4f46e5", "#7c3aed", "#0891b2", "#10b981"][:len(department_rate)])
            ax.set_xlabel("Attrition Rate (%)", fontsize=8, color="#64748b")
            ax.tick_params(axis="both", labelsize=8, colors="#475569")
            ax.grid(axis="x", alpha=.15)
            ax.set_axisbelow(True)
            for bar in bars:
                ax.text(bar.get_width()+.25, bar.get_y()+bar.get_height()/2, f"{bar.get_width():.1f}%", va="center", fontsize=8, fontweight="bold", color="#312e81")
            for spine in ax.spines.values(): spine.set_visible(False)
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        # --------------------------------------------------
        # SECOND ROW
        # --------------------------------------------------
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("⏰ Attrition by Overtime")

            overtime_rate = (
                filtered_dashboard.groupby("OverTime")["Attrition"]
                .apply(lambda x: (x == "Yes").mean() * 100)
            )

            fig, ax = plt.subplots(figsize=(5.0, 2.35))
            fig.patch.set_alpha(0)
            bars = ax.bar(overtime_rate.index, overtime_rate.values, color=["#f97316", "#ef4444"][:len(overtime_rate)], width=.55)
            ax.set_ylabel("Attrition Rate (%)", fontsize=8, color="#64748b")
            ax.tick_params(labelsize=8, colors="#475569")
            ax.grid(axis="y", alpha=.15)
            ax.set_axisbelow(True)
            for bar in bars:
                ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+.5, f"{bar.get_height():.1f}%", ha="center", fontsize=8, fontweight="bold", color="#c2410c")
            for spine in ax.spines.values(): spine.set_visible(False)
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        with col2:
            st.subheader("💼 Attrition by Job Role")

            role_rate = (
                filtered_dashboard.groupby("JobRole")["Attrition"]
                .apply(lambda x: (x == "Yes").mean() * 100)
                .sort_values(ascending=True)
            )

            fig, ax = plt.subplots(figsize=(5.0, 2.35))
            fig.patch.set_alpha(0)
            bars = ax.barh(role_rate.index, role_rate.values, color="#8b5cf6")
            ax.set_xlabel("Attrition Rate (%)", fontsize=8, color="#64748b")
            ax.tick_params(axis="both", labelsize=7, colors="#475569")
            ax.grid(axis="x", alpha=.15)
            ax.set_axisbelow(True)
            for bar in bars:
                ax.text(bar.get_width()+.25, bar.get_y()+bar.get_height()/2, f"{bar.get_width():.1f}%", va="center", fontsize=7, fontweight="bold", color="#6d28d9")
            for spine in ax.spines.values(): spine.set_visible(False)
            fig.tight_layout()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

        # --------------------------------------------------
        # QUICK INSIGHT
        # --------------------------------------------------
        st.markdown(
            f"""
            <div style="
                background:#ffffff;
                border:1px solid #e6eaf0;
                border-radius:12px;
                padding:10px 14px;
                margin-top:8px;
                box-shadow:0 3px 10px rgba(15,23,42,.04);
                font-size:12px;">
                <b>💡 Live Dashboard Insight:</b>
                Currently viewing <b>{total_employees:,}</b> employees with an
                attrition rate of <b>{attrition_rate:.2f}%</b>.
                Change the filters above to update all metrics and charts.
            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================================================
# HR ANALYTICS
# ==========================================================

elif page == "📊 HR Analytics":

    st.title("📊 Interactive HR Analytics")

    st.write(
        "Explore employee demographics, job characteristics, "
        "satisfaction and attrition patterns."
    )

    st.sidebar.subheader("🔎 Filters")

    selected_department = st.sidebar.multiselect(
        "Department",
        sorted(df["Department"].unique()),
        default=sorted(df["Department"].unique())
    )

    selected_jobrole = st.sidebar.multiselect(
        "Job Role",
        sorted(df["JobRole"].unique()),
        default=sorted(df["JobRole"].unique())
    )

    selected_overtime = st.sidebar.multiselect(
        "OverTime",
        sorted(df["OverTime"].unique()),
        default=sorted(df["OverTime"].unique())
    )

    selected_gender = st.sidebar.multiselect(
        "Gender",
        sorted(df["Gender"].unique()),
        default=sorted(df["Gender"].unique())
    )

    filtered_df = df[
        (df["Department"].isin(selected_department)) &
        (df["JobRole"].isin(selected_jobrole)) &
        (df["OverTime"].isin(selected_overtime)) &
        (df["Gender"].isin(selected_gender))
    ]

    total = len(filtered_df)

    left = len(
        filtered_df[
            filtered_df["Attrition"] == "Yes"
        ]
    )

    stayed = total - left

    rate = (
        (left / total) * 100
        if total > 0
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "👥 Employees",
        f"{total:,}"
    )

    col2.metric(
        "🚪 Left",
        f"{left:,}"
    )

    col3.metric(
        "✅ Stayed",
        f"{stayed:,}"
    )

    col4.metric(
        "📉 Attrition Rate",
        f"{rate:.2f}%"
    )

    st.markdown("---")

    if total == 0:

        st.warning(
            "No employees match the selected filters."
        )

    else:

        st.subheader(
            "🚪 Attrition Distribution"
        )

        st.bar_chart(
            filtered_df["Attrition"].value_counts()
        )

        st.subheader(
            "🏢 Attrition Rate by Department"
        )

        department_rate = (
            filtered_df.groupby("Department")["Attrition"]
            .apply(
                lambda x: (x == "Yes").mean() * 100
            )
            .sort_values(ascending=False)
        )

        st.bar_chart(department_rate)

        st.subheader(
            "💼 Attrition Rate by Job Role"
        )

        role_rate = (
            filtered_df.groupby("JobRole")["Attrition"]
            .apply(
                lambda x: (x == "Yes").mean() * 100
            )
            .sort_values(ascending=False)
        )

        st.bar_chart(role_rate)

        st.subheader(
            "⏰ Overtime vs Attrition"
        )

        overtime_rate = (
            filtered_df.groupby("OverTime")["Attrition"]
            .apply(
                lambda x: (x == "Yes").mean() * 100
            )
        )

        st.bar_chart(overtime_rate)

        st.subheader(
            "😊 Job Satisfaction vs Attrition"
        )

        satisfaction_rate = (
            filtered_df.groupby(
                "JobSatisfaction"
            )["Attrition"]
            .apply(
                lambda x: (x == "Yes").mean() * 100
            )
        )

        st.line_chart(satisfaction_rate)

        st.subheader(
            "⚖️ Work-Life Balance vs Attrition"
        )

        worklife_rate = (
            filtered_df.groupby(
                "WorkLifeBalance"
            )["Attrition"]
            .apply(
                lambda x: (x == "Yes").mean() * 100
            )
        )

        st.bar_chart(worklife_rate)

        st.subheader(
            "👤 Age Distribution"
        )

        fig, ax = plt.subplots(
            figsize=(10, 5)
        )

        ax.hist(
            filtered_df["Age"],
            bins=20
        )

        ax.set_xlabel("Age")
        ax.set_ylabel(
            "Number of Employees"
        )

        ax.set_title(
            "Employee Age Distribution"
        )

        st.pyplot(fig)

        st.subheader(
            "💰 Monthly Income by Attrition"
        )

        income_data = (
            filtered_df.groupby(
                "Attrition"
            )["MonthlyIncome"]
            .agg(
                ["mean", "median", "min", "max"]
            )
            .round(2)
        )

        st.dataframe(
            income_data,
            use_container_width=True
        )

        st.subheader(
            "📋 Employee Data"
        )

        st.dataframe(
            filtered_df,
            use_container_width=True
        )


# ==========================================================
# ATTRITION INSIGHTS
# ==========================================================

elif page == "💡 Attrition Insights":

    st.title("💡 Key Attrition Insights")

    st.write(
        "Important patterns identified from the HR dataset."
    )

    overtime_rates = (
        df.groupby("OverTime")["Attrition"]
        .apply(
            lambda x: (x == "Yes").mean() * 100
        )
    )

    overtime_yes = overtime_rates.get(
        "Yes",
        0
    )

    overtime_no = overtime_rates.get(
        "No",
        0
    )

    st.subheader("⏰ Overtime")

    st.info(
        f"Employees working overtime have an attrition "
        f"rate of {overtime_yes:.2f}%, compared with "
        f"{overtime_no:.2f}% for employees not working overtime."
    )

    department_rates = (
        df.groupby("Department")["Attrition"]
        .apply(
            lambda x: (x == "Yes").mean() * 100
        )
        .sort_values(ascending=False)
    )

    highest_department = (
        department_rates.index[0]
    )

    highest_department_rate = (
        department_rates.iloc[0]
    )

    st.subheader("🏢 Department")

    st.info(
        f"{highest_department} has the highest "
        f"department-level attrition rate at "
        f"{highest_department_rate:.2f}%."
    )

    role_rates = (
        df.groupby("JobRole")["Attrition"]
        .apply(
            lambda x: (x == "Yes").mean() * 100
        )
        .sort_values(ascending=False)
    )

    highest_role = role_rates.index[0]

    highest_role_rate = role_rates.iloc[0]

    st.subheader("💼 Job Role")

    st.info(
        f"{highest_role} has the highest "
        f"job-role attrition rate at "
        f"{highest_role_rate:.2f}%."
    )

    satisfaction_rates = (
        df.groupby(
            "JobSatisfaction"
        )["Attrition"]
        .apply(
            lambda x: (x == "Yes").mean() * 100
        )
    )

    highest_satisfaction_level = (
        satisfaction_rates.idxmax()
    )

    highest_satisfaction_attrition = (
        satisfaction_rates.max()
    )

    st.subheader("😊 Job Satisfaction")

    st.info(
        f"Satisfaction level "
        f"{highest_satisfaction_level} has an "
        f"attrition rate of "
        f"{highest_satisfaction_attrition:.2f}%."
    )

    st.warning(
        "These relationships are observations from "
        "the dataset and do not prove that a factor "
        "directly causes attrition."
    )


# ==========================================================
# EMPLOYEE RISK & PERFORMANCE
# ==========================================================

elif page == "👤 Employee Risk & Performance":

    st.title(
        "👤 Employee Risk & Performance"
    )

    st.write(
        "Select an employee to view their HR profile, "
        "attrition risk and performance indicators."
    )

    st.info(
        "Employee numbers are used as identifiers because "
        "the dataset does not contain employee names."
    )

    st.markdown("---")

    # ------------------------------------------------------
    # EMPLOYEE SELECTION
    # ------------------------------------------------------

    employee_numbers = sorted(
        df["EmployeeNumber"].unique()
    )

    selected_employee = st.selectbox(
        "🔎 Select Employee",
        employee_numbers
    )

    employee = df[
        df["EmployeeNumber"] ==
        selected_employee
    ].iloc[0]

    st.markdown("---")

    # ------------------------------------------------------
    # EMPLOYEE PROFILE
    # ------------------------------------------------------

    st.subheader("👤 Employee Profile")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Employee Number",
        str(employee["EmployeeNumber"])
    )

    col2.metric(
        "Age",
        str(employee["Age"])
    )

    col3.metric(
        "Department",
        employee["Department"]
    )

    col4.metric(
        "Job Role",
        employee["JobRole"]
    )

    st.markdown("---")

    # ------------------------------------------------------
    # BUILD MODEL INPUT
    # ------------------------------------------------------

    prediction_columns = [
        "Age",
        "BusinessTravel",
        "DailyRate",
        "Department",
        "DistanceFromHome",
        "Education",
        "EducationField",
        "EnvironmentSatisfaction",
        "Gender",
        "HourlyRate",
        "JobInvolvement",
        "JobLevel",
        "JobRole",
        "JobSatisfaction",
        "MaritalStatus",
        "MonthlyIncome",
        "MonthlyRate",
        "NumCompaniesWorked",
        "OverTime",
        "PercentSalaryHike",
        "PerformanceRating",
        "RelationshipSatisfaction",
        "StockOptionLevel",
        "TotalWorkingYears",
        "TrainingTimesLastYear",
        "WorkLifeBalance",
        "YearsAtCompany",
        "YearsInCurrentRole",
        "YearsSinceLastPromotion",
        "YearsWithCurrManager"
    ]

    employee_input = pd.DataFrame(
        [employee[prediction_columns].to_dict()]
    )

    # ------------------------------------------------------
    # PREDICTION
    # ------------------------------------------------------

    prediction = model.predict(
        employee_input
    )[0]

    probability = model.predict_proba(
        employee_input
    )[0][1]

    probability_percentage = (
        probability * 100
    )

    # ------------------------------------------------------
    # RISK LEVEL
    # ------------------------------------------------------

    if probability_percentage < 30:

        risk_level = "LOW RISK"

    elif probability_percentage < 60:

        risk_level = "MEDIUM RISK"

    else:

        risk_level = "HIGH RISK"

    # ------------------------------------------------------
    # MAIN RISK CARDS
    # ------------------------------------------------------

    st.subheader("🚦 Employee Risk Assessment")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Attrition Probability",
        f"{probability_percentage:.2f}%"
    )

    col2.metric(
        "Risk Level",
        risk_level
    )

    if prediction == 1:

        prediction_text = "Likely to Leave"

    else:

        prediction_text = "Likely to Stay"

    col3.metric(
        "Model Prediction",
        prediction_text
    )

    st.progress(
        float(probability)
    )

    if probability_percentage < 30:

        st.success(
            "🟢 LOW ATTRITION RISK"
        )

    elif probability_percentage < 60:

        st.warning(
            "🟡 MEDIUM ATTRITION RISK"
        )

    else:

        st.error(
            "🔴 HIGH ATTRITION RISK"
        )

    st.markdown("---")

    # ------------------------------------------------------
    # PERFORMANCE
    # ------------------------------------------------------

    st.subheader(
        "⭐ Employee Performance & Work Indicators"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Performance Rating",
        f"{employee['PerformanceRating']}/4"
    )

    col2.metric(
        "Job Involvement",
        f"{employee['JobInvolvement']}/4"
    )

    col3.metric(
        "Job Satisfaction",
        f"{employee['JobSatisfaction']}/4"
    )

    col4.metric(
        "Environment Satisfaction",
        f"{employee['EnvironmentSatisfaction']}/4"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Work-Life Balance",
        f"{employee['WorkLifeBalance']}/4"
    )

    col2.metric(
        "Relationship Satisfaction",
        f"{employee['RelationshipSatisfaction']}/4"
    )

    col3.metric(
        "Overtime",
        employee["OverTime"]
    )

    col4.metric(
        "Years at Company",
        str(employee["YearsAtCompany"])
    )

    st.markdown("---")

    # ------------------------------------------------------
    # CAREER INFORMATION
    # ------------------------------------------------------

    st.subheader(
        "📈 Career Information"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Job Level",
        str(employee["JobLevel"])
    )

    col2.metric(
        "Total Working Years",
        str(employee["TotalWorkingYears"])
    )

    col3.metric(
        "Years in Current Role",
        str(employee["YearsInCurrentRole"])
    )

    col4.metric(
        "Years Since Promotion",
        str(employee["YearsSinceLastPromotion"])
    )

    st.markdown("---")

    # ------------------------------------------------------
    # FINANCIAL INFORMATION
    # ------------------------------------------------------

    st.subheader(
        "💰 Compensation Information"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Monthly Income",
        f"{employee['MonthlyIncome']:,}"
    )

    col2.metric(
        "Monthly Rate",
        f"{employee['MonthlyRate']:,}"
    )

    col3.metric(
        "Salary Hike",
        f"{employee['PercentSalaryHike']}%"
    )

    st.markdown("---")

    # ------------------------------------------------------
    # HR RECOMMENDATIONS
    # ------------------------------------------------------

    st.subheader(
        "💡 HR Recommendations"
    )

    recommendations = []

    if probability_percentage >= 60:

        recommendations.append(
            "Review workload and overtime requirements."
        )

        recommendations.append(
            "Discuss career growth and promotion opportunities."
        )

        recommendations.append(
            "Review employee satisfaction and engagement."
        )

    elif probability_percentage >= 30:

        recommendations.append(
            "Monitor employee engagement regularly."
        )

        recommendations.append(
            "Discuss career goals and development opportunities."
        )

        recommendations.append(
            "Review workload and work-life balance."
        )

    else:

        recommendations.append(
            "Continue employee engagement activities."
        )

        recommendations.append(
            "Maintain a healthy work environment."
        )

        recommendations.append(
            "Continue providing career development opportunities."
        )

    if employee["OverTime"] == "Yes":

        recommendations.append(
            "Consider reviewing overtime workload."
        )

    if employee["JobSatisfaction"] <= 2:

        recommendations.append(
            "Consider a discussion about job satisfaction."
        )

    if employee["WorkLifeBalance"] <= 2:

        recommendations.append(
            "Review work-life balance concerns."
        )

    for recommendation in recommendations:

        st.write(
            "• " + recommendation
        )

    st.markdown("---")

    # ------------------------------------------------------
    # EMPLOYEE COMPLETE DATA
    # ------------------------------------------------------

    with st.expander(
        "📋 View Complete Employee Data"
    ):

        st.dataframe(
            employee.to_frame(
                name="Value"
            ),
            use_container_width=True
        )


# ==========================================================
# ATTRITION PREDICTION
# ==========================================================

elif page == "🤖 Attrition Prediction":

    st.title(
        "🤖 Employee Attrition Prediction"
    )

    st.write(
        "Enter employee information to estimate "
        "the probability of attrition."
    )

    st.warning(
        "The result is a machine-learning estimate "
        "and should not be treated as a certainty "
        "or standalone HR decision."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "👤 Employee Information"
        )

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=60,
            value=30
        )

        gender = st.selectbox(
            "Gender",
            sorted(df["Gender"].unique())
        )

        marital_status = st.selectbox(
            "Marital Status",
            sorted(df["MaritalStatus"].unique())
        )

        business_travel = st.selectbox(
            "Business Travel",
            sorted(df["BusinessTravel"].unique())
        )

        department = st.selectbox(
            "Department",
            sorted(df["Department"].unique())
        )

        education = st.selectbox(
            "Education",
            sorted(df["Education"].unique())
        )

        education_field = st.selectbox(
            "Education Field",
            sorted(df["EducationField"].unique())
        )

        distance_from_home = st.number_input(
            "Distance From Home",
            min_value=1,
            max_value=30,
            value=5
        )

        job_role = st.selectbox(
            "Job Role",
            sorted(df["JobRole"].unique())
        )

        job_level = st.selectbox(
            "Job Level",
            sorted(df["JobLevel"].unique())
        )

        overtime = st.selectbox(
            "OverTime",
            sorted(df["OverTime"].unique())
        )

    with col2:

        st.subheader(
            "💼 Work Information"
        )

        daily_rate = st.number_input(
            "Daily Rate",
            min_value=102,
            max_value=1499,
            value=800
        )

        hourly_rate = st.number_input(
            "Hourly Rate",
            min_value=30,
            max_value=100,
            value=65
        )

        monthly_income = st.number_input(
            "Monthly Income",
            min_value=1000,
            max_value=20000,
            value=5000
        )

        monthly_rate = st.number_input(
            "Monthly Rate",
            min_value=2000,
            max_value=27000,
            value=14000
        )

        num_companies = st.number_input(
            "Number of Companies Worked",
            min_value=0,
            max_value=10,
            value=2
        )

        total_working_years = st.number_input(
            "Total Working Years",
            min_value=0,
            max_value=40,
            value=8
        )

        years_at_company = st.number_input(
            "Years at Company",
            min_value=0,
            max_value=40,
            value=5
        )

        years_current_role = st.number_input(
            "Years in Current Role",
            min_value=0,
            max_value=18,
            value=3
        )

        years_since_promotion = st.number_input(
            "Years Since Last Promotion",
            min_value=0,
            max_value=15,
            value=2
        )

        years_manager = st.number_input(
            "Years With Current Manager",
            min_value=0,
            max_value=17,
            value=3
        )

        environment_satisfaction = st.selectbox(
            "Environment Satisfaction",
            sorted(df["EnvironmentSatisfaction"].unique())
        )

        job_involvement = st.selectbox(
            "Job Involvement",
            sorted(df["JobInvolvement"].unique())
        )

        job_satisfaction = st.selectbox(
            "Job Satisfaction",
            sorted(df["JobSatisfaction"].unique())
        )

        relationship_satisfaction = st.selectbox(
            "Relationship Satisfaction",
            sorted(df["RelationshipSatisfaction"].unique())
        )

        work_life_balance = st.selectbox(
            "Work-Life Balance",
            sorted(df["WorkLifeBalance"].unique())
        )

    st.markdown("---")

    if st.button(
        "🔮 PREDICT ATTRITION RISK",
        use_container_width=True
    ):

        input_data = pd.DataFrame({

            "Age": [age],
            "BusinessTravel": [business_travel],
            "DailyRate": [daily_rate],
            "Department": [department],
            "DistanceFromHome": [distance_from_home],
            "Education": [education],
            "EducationField": [education_field],
            "EnvironmentSatisfaction": [
                environment_satisfaction
            ],
            "Gender": [gender],
            "HourlyRate": [hourly_rate],
            "JobInvolvement": [job_involvement],
            "JobLevel": [job_level],
            "JobRole": [job_role],
            "JobSatisfaction": [job_satisfaction],
            "MaritalStatus": [marital_status],
            "MonthlyIncome": [monthly_income],
            "MonthlyRate": [monthly_rate],
            "NumCompaniesWorked": [num_companies],
            "OverTime": [overtime],
            "PercentSalaryHike": [
                df["PercentSalaryHike"].median()
            ],
            "PerformanceRating": [
                df["PerformanceRating"].median()
            ],
            "RelationshipSatisfaction": [
                relationship_satisfaction
            ],
            "StockOptionLevel": [
                df["StockOptionLevel"].median()
            ],
            "TotalWorkingYears": [
                total_working_years
            ],
            "TrainingTimesLastYear": [
                df["TrainingTimesLastYear"].median()
            ],
            "WorkLifeBalance": [
                work_life_balance
            ],
            "YearsAtCompany": [
                years_at_company
            ],
            "YearsInCurrentRole": [
                years_current_role
            ],
            "YearsSinceLastPromotion": [
                years_since_promotion
            ],
            "YearsWithCurrManager": [
                years_manager
            ]
        })

        prediction = model.predict(
            input_data
        )[0]

        probability = model.predict_proba(
            input_data
        )[0][1]

        percentage = probability * 100

        if percentage < 30:

            risk = "LOW RISK"

            st.success(
                "🟢 LOW ATTRITION RISK"
            )

        elif percentage < 60:

            risk = "MEDIUM RISK"

            st.warning(
                "🟡 MEDIUM ATTRITION RISK"
            )

        else:

            risk = "HIGH RISK"

            st.error(
                "🔴 HIGH ATTRITION RISK"
            )

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Prediction",
            "Likely to Leave"
            if prediction == 1
            else "Likely to Stay"
        )

        col2.metric(
            "Attrition Probability",
            f"{percentage:.2f}%"
        )

        col3.metric(
            "Risk Level",
            risk
        )

        st.progress(
            float(probability)
        )


# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

elif page == "📈 Model Performance":

    st.title(
        "📈 Machine Learning Model Performance"
    )

    results = pd.DataFrame({

        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest"
        ],

        "Accuracy": [
            0.7517,
            0.7687,
            0.8299
        ],

        "Precision": [
            0.3488,
            0.3562,
            0.4571
        ],

        "Recall": [
            0.6383,
            0.5532,
            0.3404
        ],

        "F1 Score": [
            0.4511,
            0.4333,
            0.3902
        ]
    })

    st.dataframe(
        results.style.format(
            {
                "Accuracy": "{:.2%}",
                "Precision": "{:.2%}",
                "Recall": "{:.2%}",
                "F1 Score": "{:.2%}"
            }
        ),
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "🏆 Selected Model"
    )

    st.success(
        """
        Logistic Regression was selected because it achieved
        the highest F1-score among the evaluated models and
        provided higher recall for the Attrition class.
        """
    )

    st.subheader(
        "📊 Model Comparison"
    )

    chart_data = results.set_index(
        "Model"
    )[
        [
            "Accuracy",
            "Precision",
            "Recall",
            "F1 Score"
        ]
    ]

    st.bar_chart(chart_data)

    st.subheader(
        "🔢 Logistic Regression Confusion Matrix"
    )

    confusion = pd.DataFrame(
        [
            [191, 56],
            [17, 30]
        ],
        index=[
            "Actual: No Attrition",
            "Actual: Attrition"
        ],
        columns=[
            "Predicted: No Attrition",
            "Predicted: Attrition"
        ]
    )

    st.dataframe(
        confusion,
        use_container_width=True
    )

    st.info(
        "Because the dataset contains substantially more "
        "employees who stayed than employees who left, "
        "accuracy alone is not sufficient. Recall and "
        "F1-score are also important."
    )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    "HR Analytics & Employee Attrition Prediction | "
    "Python • Pandas • Scikit-learn • Streamlit"
)

