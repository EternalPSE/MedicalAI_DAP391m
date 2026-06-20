# Patient Readmission Prediction with Explainable AI

**Course:** On-going Assessment
**Project title:** Patient Readmission Prediction with Explainable AI

## Project Overview

This repository contains the foundation for a healthcare data science project. The project goal is to prepare and understand hospital/patient data so that later stages can build a machine learning model to predict whether a patient may be readmitted.

Explainable AI is included as the project direction because healthcare predictions should not be treated as a black box. Doctors, nurses, hospital managers, and data analysts need to understand which factors influence readmission risk before using a model to support decision-making.

## Scope

This project follows the early project workflow: project topic selection, project planning, business understanding, data understanding, importing datasets, data wrangling, and preprocessing.

The work intentionally stays at an early project stage. It does not focus on deployment or advanced explainability yet. A simple baseline model is included only as a preview when a valid readmission target column exists.

## Business Problem

Hospital readmission can create extra pressure on hospital resources and may indicate that patients need better discharge planning or follow-up care. This project studies patient data to prepare for a prediction system that can estimate readmission risk and later explain the main factors behind that risk.

Expected business value:

* Reduce unnecessary readmission
* Improve patient care planning
* Support hospital resource allocation
* Help healthcare staff understand important readmission-related factors

## Dataset Source

The dataset source is from Kaggle:

`vanpatangan/readmission-dataset`

For this project, three CSV files can be uploaded manually for easier use. The notebook first searches for CSV files in:

* the current working directory
* `data/raw/`
* `/mnt/data/` for notebook environments

If no CSV files are found, the notebook uses KaggleHub as a backup download method.

## Repository Structure

```text
Patient-Readmission-Prediction-XAI/
│
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   └── .gitkeep
│   ├── processed/
│   │   └── .gitkeep
│
├── notebooks/
│   └── Patient_Readmission_EDA_Preprocessing.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── utils.py
│
├── reports/
│   └── Report.md
│
└── outputs/
    ├── figures/
    │   └── .gitkeep
    └── processed_data/
        └── .gitkeep
```

## How to Run the Project

1. Clone or download this repository.
2. Place the three CSV files in `data/raw/` or upload them to the notebook environment.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Open the notebook:

```bash
jupyter notebook notebooks/Patient_Readmission_EDA_Preprocessing.ipynb
```

5. Run all cells from top to bottom.

The processed dataset will be saved to:

```text
outputs/processed_data/processed_readmission.csv
```

Figures generated during EDA will be saved to:

```text
outputs/figures/
```

## Main Tasks

* Introduce the project topic
* Explain the business understanding
* Describe the dataset source
* Import Dataset 1, Dataset 2, and Dataset 3
* Understand data shape, data types, missing values, duplicates, and basic statistics
* Clean column names
* Handle duplicates and simple missing values
* Identify the readmission target column if available
* Encode categorical variables for later modeling
* Save the processed dataset
* Create simple exploratory visualizations
* Prepare a clear plan for later machine learning and Explainable AI work

## Future Work

Later we can continue with:

* Better feature engineering
* More careful model comparison
* Hyperparameter tuning
* Model evaluation using healthcare-oriented metrics
* Explainable AI using feature importance, permutation importance, SHAP, or LIME
* Final report and presentation
