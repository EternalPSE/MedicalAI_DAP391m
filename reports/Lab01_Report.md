# Lab01 Report: Patient Readmission Prediction with Explainable AI

## 1. Introduction

This Lab01 report introduces the project **Patient Readmission Prediction with Explainable AI**. The project studies hospital and patient data to prepare for a later machine learning model that can predict whether a patient may be readmitted.

Because this is Lab01, the main work focuses on project introduction, business understanding, data understanding, dataset importing, data wrangling, preprocessing, and a clear plan for later machine learning and Explainable AI stages.

## 2. Business Understanding

Patient readmission is an important healthcare problem because it can increase hospital workload, cost, and patient risk. A prediction model may help hospitals identify patients who need better discharge planning or follow-up care.

Main stakeholders include:

- Hospital management
- Doctors
- Nurses
- Data analysts
- Patients

Expected business value:

- Reduce unnecessary readmission
- Improve patient care planning
- Support hospital resource allocation
- Make readmission risk factors easier to understand

## 3. Data Source

The dataset comes from Kaggle:

`vanpatangan/readmission-dataset`

For easier use, three CSV files can be uploaded manually. The notebook first searches for uploaded CSV files in the current directory, `data/raw/`, and `/mnt/data/`. If CSV files are not found, KaggleHub is used as a backup download method.

## 4. Data Understanding

The notebook analyzes each available CSV file separately. For each dataset, it checks:

- Dataset shape
- Column names
- Data types
- Missing values
- Duplicate rows
- Descriptive statistics
- Numeric and categorical columns

This step helps the team understand what information is available before doing preprocessing or modeling.

## 5. Data Wrangling and Preprocessing

The Lab01 preprocessing steps are simple and transparent:

- Clean column names by using lowercase and underscores
- Remove duplicate rows
- Fill missing numeric values using the median
- Fill missing categorical values using the mode or `Unknown`
- Parse possible date columns when suitable
- Detect the likely readmission target column programmatically
- Encode categorical variables with `pandas.get_dummies`
- Save the processed dataset to `outputs/processed_data/processed_readmission_lab01.csv`

The preprocessing does not remove too much data because Lab01 is mainly about building a clean foundation.

## 6. Initial Findings

The initial findings should be updated after running the notebook on the uploaded CSV files. In general, this section should describe:

- Which CSV file is most relevant for prediction
- Whether a readmission target column exists
- Which columns are numeric and categorical
- Whether missing values or duplicated rows exist
- What the basic target distribution looks like

## 7. Project Plan

| Phase | Description | Lab Stage |
|---|---|---|
| Phase 1 | Business understanding | Lab01 |
| Phase 2 | Data understanding | Lab01 |
| Phase 3 | Data preprocessing | Lab01 |
| Phase 4 | Baseline modeling | Later lab / preview |
| Phase 5 | Model evaluation | Later lab |
| Phase 6 | Explainable AI | Later lab |
| Phase 7 | Final report and presentation | Final stage |

## 8. Conclusion

Lab01 prepares the early foundation for the patient readmission project. The repository includes code for importing datasets, checking data quality, cleaning data, performing simple exploratory analysis, and saving a processed dataset. The project is ready to continue with stronger modeling and Explainable AI in later labs.
