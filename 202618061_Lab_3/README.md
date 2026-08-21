# Lab 3 - Scikit-learn Preprocessing and Model Evaluation

## Student Information

- **Name:** Vedant Kapur
- **Student ID:** 202618061
- **Course:** Machine Learning
---

## 1. Objective

The objective of this lab is to build and compare Scikit-learn preprocessing pipelines and evaluate two classification models on the Hotel Booking Demand dataset.

Two preprocessing pipelines were created:

- Pipeline A: KNNImputer + StandardScaler
- Pipeline B: KNNImputer + MinMaxScaler

Two classification models were evaluated using both pipelines:

- Logistic Regression
- Decision Tree

This resulted in four model-pipeline combinations.

---

## 2. Dataset

### Hotel Booking Demand Dataset

The dataset contains hotel booking information and is used to predict whether a hotel booking will be canceled.

- **Dataset:** Hotel Booking Demand
- **File:** `hotel_bookings.csv`
- **Target Variable:** `is_canceled`

### Dataset Link

**[PASTE THE ACTUAL DATASET LINK YOU USED HERE]**

---

## 3. Dataset Understanding

The dataset was loaded using Pandas and examined using:

- `head()`
- `shape`
- `info()`
- `describe()`
- `dtypes`

The target variable `is_canceled` was used for classification.

The target values represent:

- `0` → Booking was not canceled
- `1` → Booking was canceled

The dataset was separated into:

- `X` → input features
- `y` → target variable

Numerical and categorical features were identified using Pandas data types.

---

## 4. Data Cleaning and Preprocessing

### Missing Values

Missing values were examined by calculating both the missing-value count and missing-value percentage for every column.

Columns with very high missingness were identified.

The `company` column was removed because it contains an extremely high proportion of missing values, making it unsuitable as a useful predictive feature.

Other missing values were not manually filled during the cleaning stage because the assignment required missing-value handling to be performed inside the Scikit-learn preprocessing pipelines.

---

### Data Leakage

The following columns were removed:

- `reservation_status`
- `reservation_status_date`

These variables directly reveal information about the final booking outcome and could therefore cause data leakage when predicting `is_canceled`.

---

### Outlier Detection

Selected numerical features were examined using boxplots and the IQR method.

The selected features were:

- `lead_time`
- `adr`
- `adults`
- `children`
- `babies`

A stricter `3 × IQR` threshold was used to identify clear and extreme outliers.

Only observations outside these extreme boundaries were removed.

- **Rows before outlier removal:** [FILL AFTER RUNNING]
- **Rows after outlier removal:** [FILL AFTER RUNNING]
- **Rows removed:** [FILL AFTER RUNNING]

The cleaned dataset used for modeling is provided as:

`cleaned_hotel_bookings.csv`

---

## 5. Train-Test Split

The same train-test split was used for all experiments to ensure a fair comparison.

```text
test_size = 0.2
stratify = y
random_state = 42