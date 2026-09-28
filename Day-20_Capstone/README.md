# Loan Approval Analysis

**CodeTrade AI/ML Internship — Phase 1 Capstone**

## Project Overview

This project analyzes loan application data to identify applicant characteristics associated with loan approval.

The analysis focuses on factors such as Credit History, Applicant Income, Education, and Loan Amount. It uses data cleaning, exploratory data analysis (EDA), data visualization, and statistical hypothesis testing to identify patterns in loan approval.

**Research Question:** Which applicant characteristics are most strongly associated with loan approval?

## Dataset

The project uses a loan approval dataset containing **614 loan applications and 13 columns**.

* **Total applications:** 614
* **Total columns:** 13
* **Target variable:** `Loan_Status`
* **Approval categories:** Approved (`Y`) and Rejected (`N`)


## Tools and Technologies

* **Python** — Programming language
* **Pandas** — Data manipulation and analysis
* **NumPy** — Numerical computations
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization
* **SciPy** — Statistical hypothesis testing
* **Jupyter Notebook** — Interactive analysis

## Project Workflow

1. **Data Loading:** Loaded the loan approval dataset using Pandas.
2. **Data Cleaning:** Checked missing values, handled missing data, and treated selected numerical outliers.
3. **Exploratory Data Analysis:** Examined applicant characteristics and their relationships with loan approval.
4. **Data Visualization:** Created charts to identify patterns and compare applicant groups.
5. **Statistical Hypothesis Testing:** Used statistical tests to investigate associations and differences between approved and rejected applications.
6. **Interpretation:** Summarized the findings while considering the limitations of the analysis.

## Data Cleaning Decisions

The following cleaning decisions were used in the analysis:

* **Missing Credit History:** Missing values in `Credit_History` were filled with `0`. This treats missing values as having no positive credit history and may affect the observed association with loan approval.
* **Outlier Detection:** Potential outliers in `ApplicantIncome`, `CoapplicantIncome`, and `LoanAmount` were identified using the Interquartile Range (IQR) method.
* **Outlier Treatment:** The identified outliers were replaced with median values.
* **Data Preparation:** Missing values and data types were checked before conducting the analysis.

These decisions may influence the distributions, statistical tests, and findings.

## Key Findings

### 1. Credit History

Credit History showed a statistically significant association with loan approval.

Applicants with `Credit_History = 1` had substantially more approvals than rejections.

* **Chi-square statistic:** 112.6953
* **p-value:** 2.516 × 10⁻²⁶
* **Cramér’s V:** 0.4284

The results indicate an association between Credit History and Loan Status in this dataset. They do not establish that Credit History alone causes loan approval.

### 2. Applicant Income

Welch’s t-test did not find a statistically significant difference in mean Applicant Income between approved and rejected applicants.

* **Welch’s t-test p-value:** 0.6910
* **Cohen’s d:** 0.0343
* **Mann–Whitney U test p-value:** 0.9345

The Mann–Whitney U test also did not provide sufficient evidence of a difference between the two groups. This provides a useful comparison because Applicant Income is heavily right-skewed.

### 3. Applicant Income and Loan Amount

A positive correlation of approximately **0.303** was observed between Applicant Income and Loan Amount.

This indicates that applicants with higher incomes tended to have higher loan amounts in the analyzed dataset.

Correlation does not imply causation.

### 4. Education

The analysis explored Education in relation to applicant income and loan approval. The observed patterns are descriptive and do not establish that Education causes approval or rejection.

## Conclusion

Credit History showed a statistically significant association with loan approval. In contrast, Applicant Income did not show a statistically significant difference between approved and rejected applicants in the hypothesis tests performed.

Applicant Income and Loan Amount showed a positive relationship. Overall, this project provided practical experience in data cleaning, exploratory data analysis, data visualization, and statistical hypothesis testing using Python.

## Limitations

* **Missing Credit History values:** Missing values in `Credit_History` were filled with `0` instead of the most frequent value. Using the mode or another imputation method could change the results of the Credit History analysis.
* **Outlier treatment:** Replacing potential outliers in `ApplicantIncome`, `CoapplicantIncome`, and `LoanAmount` with median values may affect the distributions and statistical results.
* **Skewed income distribution:** Applicant Income is heavily right-skewed. Although the Mann–Whitney U test was also performed, the interpretation of statistical results depends on the assumptions and characteristics of each test.
* **Dataset size and representativeness:** The dataset contains 614 applications and may not represent all applicants, banks, or lending practices.
* **Association versus causation:** The analysis identifies associations and differences but cannot establish that any applicant characteristic causes loan approval.
* **Unobserved factors:** The dataset may not include every factor used in real-world loan approval decisions.

## How to Run the Project

### Prerequisites

Install Python and ensure that Jupyter Notebook is available.

### 1. Clone or Download the Repository

Download the project repository or clone it using Git:

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd Day-20_Capstone
```

### 2. Install the Required Libraries

Install the dependencies using:

```bash
pip install -r requirements.txt
```

### 3. Check the Dataset

Ensure that `loan_approved.csv` is present in the project directory.

If your dataset has a different filename or location, update the file path in the notebook.

### 4. Open Jupyter Notebook

Run:

```bash
jupyter notebook
```

Open `project.ipynb`.

### 5. Run the Analysis

In Jupyter Notebook, select **Kernel → Restart Kernel and Run All**.

Ensure that all cells execute successfully from beginning to end.

## Project Structure

```text
Day-20_Capstone/
│
├── loan_approved.csv
├── project.ipynb
├── README.md
├── requirements.txt
│
└── figures/
    ├── chart_1_loan_approval_distribution.png
    ├── chart_2_Applicant_income_distribution.png
    ├── chart_3_Applicantincome_loanAmount.png
    ├── chart_4_credit_history.png
    ├── chart_5_ApplicanIncome_LoanStatus.png
    ├── chart_6_Education_ApplicantIncome.png
    ├── chart_7_Approval_Rate_Education.png
    └── chart_8_heatmap.png
```

## Visualizations

The project includes the following eight visualizations:

1. `chart_1_loan_approval_distribution.png` — Loan Approval Distribution
2. `chart_2_Applicant_income_distribution.png` — Applicant Income Distribution
3. `chart_3_Applicantincome_loanAmount.png` — Applicant Income vs. Loan Amount
4. `chart_4_credit_history.png` — Credit History
5. `chart_5_ApplicanIncome_LoanStatus.png` — Applicant Income by Loan Status
6. `chart_6_Education_ApplicantIncome.png` — Education and Applicant Income
7. `chart_7_Approval_Rate_Education.png` — Approval Rate by Education
8. `chart_8_heatmap.png` — Correlation Heatmap
