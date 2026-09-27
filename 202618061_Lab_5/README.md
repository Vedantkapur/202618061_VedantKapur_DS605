
# DS605 Lab 5 — Machine Learning with Scikit-learn and From Scratch

This repository implements the complete DS605 Lab-5 workflow on the **UCI Productivity Prediction of Garment Employees** dataset.

## Assignment requirements covered

### Part A — Scikit-learn
- Missing-value handling
- Categorical encoding
- Feature scaling
- One fixed train-test split
- Linear Regression
- Logistic Regression
- MAE, RMSE, R²
- Accuracy, Precision, Recall, F1
- Training and prediction timing

### Part B — From Scratch
Only **NumPy and Pandas** are used for the machine-learning implementation.
The manual section implements:
- missing-value handling
- categorical one-hot encoding
- feature scaling
- Linear Regression
- sigmoid
- Logistic Regression
- gradient descent
- probability prediction
- thresholding
- all required metrics

### Part C — Comparison and Optimization
- Same test samples are reused
- Manual Logistic Regression is tuned using a validation portion taken ONLY from the training data
- Learning rate and L2 regularization are selected automatically
- Comparison CSV files are generated

## Dataset

Download `garments_worker_productivity.csv` from the UCI Productivity Prediction of Garment Employees dataset and place it in the repository root.

The UCI dataset contains 1,197 instances and includes production features such as department, team, targeted productivity, SMV, WIP, overtime, incentives, number of workers, and actual productivity.

Source:
https://archive.ics.uci.edu/dataset/597/productivity+prediction+of+garment+employees

## Folder layout

```text
DS605-Lab5/
│
├── garments_worker_productivity.csv
├── sklearn_model.py
├── from_scratch.py
├── requirements.txt
├── README.md
└── .gitignore
```

After running the programs, result files are also generated:

```text
split_indices.csv
sklearn_regression_results.csv
sklearn_classification_results.csv
manual_regression_results.csv
manual_classification_results.csv
regression_comparison.csv
classification_comparison.csv
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

### 1. Run Part A

```bash
python sklearn_model.py
```

This creates the fixed train/test indices in:

```text
split_indices.csv
```

### 2. Run Part B + Part C

```bash
python from_scratch.py
```

The manual implementation reads the exact same indices from `split_indices.csv`.

## Why the same split matters

If sklearn and the manual implementation used different test samples, one model could appear better simply because it received an easier test set.

Therefore:

```text
Same raw data
      ↓
Same target definition
      ↓
Same train/test row indices
      ↓
Same preprocessing logic
      ↓
Different model implementation
      ↓
Fair comparison
```

## Target definitions

### Regression

```text
target = actual_productivity
```

The model predicts the continuous productivity value.

### Classification

```text
MeetsTarget = 1  if actual_productivity >= targeted_productivity
MeetsTarget = 0  otherwise
```

`actual_productivity` is NOT included as an input feature for classification.

## Preprocessing decisions

### WIP

The dataset contains missing WIP values. In this dataset an empty WIP field represents no work in progress, so the implementation fills those values with 0.

### Numerical features

Numerical columns are:
1. median-imputed if required
2. standardized using training-set mean and standard deviation

Standardization uses:

```text
z = (x - mean) / standard_deviation
```

The statistics are learned from the training set only.

### Categorical features

The categorical columns are:

```text
quarter
department
day
```

They are converted into one-hot vectors.

For example:

```text
department = sewing
department = finishing
```

becomes:

```text
sewing   finishing
1        0
0        1
```

## Linear Regression from scratch

The manual model uses Ordinary Least Squares:

```text
β = (XᵀX)⁻¹Xᵀy
```

The implementation uses:

```python
np.linalg.pinv(X) @ y
```

rather than directly computing an inverse because the pseudo-inverse is numerically safer when the matrix is singular or close to singular.

## Logistic Regression from scratch

The manual classifier uses:

```text
z = Xβ
p = sigmoid(z)

sigmoid(z) = 1 / (1 + e⁻ᶻ)
```

Then gradient descent updates the parameters:

```text
β = β - learning_rate × gradient
```

A prediction is:

```text
1 if probability >= 0.5
0 otherwise
```

L2 regularization is added to reduce excessively large weights.

## Metrics

### Regression

**MAE**

```text
mean(|actual - predicted|)
```

Lower is better.

**RMSE**

```text
sqrt(mean((actual - predicted)²))
```

Lower is better. Because errors are squared first, large errors have more influence.

**R²**

```text
1 - SSE/SST
```

Higher is generally better; 1 represents a perfect fit.

### Classification

**Accuracy**

```text
(TP + TN) / all predictions
```

**Precision**

```text
TP / (TP + FP)
```

**Recall**

```text
TP / (TP + FN)
```

**F1**

```text
2 × precision × recall / (precision + recall)
```

## Important implementation rule

`from_scratch.py` does not import or call scikit-learn. This is deliberate because the assignment explicitly prohibits sklearn preprocessing, models, metrics, and train-test utilities in the manual section.

## Final observation template

After running the code, report the actual generated values rather than inventing them.

Discuss:

1. Which implementation obtained the lower MAE/RMSE?
2. Which obtained the higher R²?
3. Which obtained the higher classification F1?
4. How much training time differed?
5. How much prediction time differed?
6. Did manual optimization improve F1/accuracy?
7. Why might sklearn still be faster despite both approaches using NumPy internally?
8. What preprocessing choices affected the results?

Do not claim that one implementation is universally superior. The comparison is specific to this dataset, split, preprocessing, hardware, and model configuration.
