# Customer Churn Prediction – Responsible ML

## Project Overview
This project demonstrates a responsible Machine Learning approach to customer churn prediction using Python and Scikit-learn.

The objective is to explore customer behaviour patterns and identify factors associated with customer churn.

## Internship Details
- Organization: RabTech Academy
- Domain: Artificial Intelligence & Machine Learning
- Task: Task 02 – ML Problem Framing & Responsible Data Card

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab
- GitHub

## Dataset Description
The supplied training dataset contains 12 customer records and 7 columns.

Features include:
- Tenure months
- Support tickets
- Monthly spending
- Last login days
- Subscription plan

Target:
- `churned` (0 = Not churned, 1 = Churned)

The customer ID is excluded from model training.

## Machine Learning Approach
1. Data loading and exploration
2. Data quality checks
3. Feature preprocessing
4. Majority-class baseline
5. Logistic Regression classification
6. Leave-One-Out Cross-Validation
7. Model evaluation

## Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

## Responsible AI Considerations
- Data privacy and protection
- Bias and fairness
- False-positive and false-negative risks
- Data leakage prevention
- Human oversight
- Model limitations

## Project Structure
```text
Customer-Churn-Responsible-ML/
│
├── README.md
├── requirements.txt
├── customer_churn_baseline_notebook.ipynb
├── customer_churn_risk_register.docx
├── customer_churn_risk_register.pdf
├── problem_framing_memo.docx
├── problem_framing_memo.pdf
├── responsible_data_card_completed.docx
└── responsible_data_card_completed.pdf
```

## Limitations
The dataset contains only 12 records. Therefore, the results are preliminary and intended for educational demonstration only. The model is not suitable for real-world deployment without further validation.

## Conclusion
This project demonstrates a basic customer churn prediction workflow while emphasizing responsible data handling, evaluation, transparency and human oversight.
---

## Task 03: Feature Engineering & Preprocessing Pipeline

### Objective
To build a reusable machine learning preprocessing pipeline using Scikit-learn.

### Dataset
UCI Adult Income Dataset (48,842 records).

### Work Completed
- Loaded and explored a real-world tabular dataset.
- Checked missing values and duplicate records.
- Separated input features and target variable.
- Performed train-test splitting before preprocessing.
- Built numerical and categorical preprocessing pipelines.
- Used SimpleImputer, StandardScaler and OneHotEncoder.
- Implemented ColumnTransformer.
- Built a complete Scikit-learn Pipeline using Logistic Regression.
- Evaluated model performance using Accuracy, Precision, Recall and F1-score.
- Visualised the confusion matrix.
- Performed permutation-based feature importance analysis.

### Technologies Used
Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook.

### Notebook
[View Task 03 Notebook](RabTech_Task03_Feature_Engineering_Preprocessing.ipynb)
