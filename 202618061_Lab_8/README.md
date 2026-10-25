# DS605 Lab Assignment 8 — Decision Trees and Support Vector Machines

## Contents
- `notebooks/DS605_Lab8_Decision_Trees_SVM.ipynb` — complete runnable assignment.
- `src/` — reserved for optional extensions; the from-scratch implementations are included in the notebook.
- `results/` — generated plots and CSV comparison tables are saved here when the notebook is run.
- `requirements.txt` — Python dependencies.
- `banknote_authentication.csv` — downloaded automatically on the first successful notebook run.

## Requirements
Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

Open and run `notebooks/DS605_Lab8_Decision_Trees_SVM.ipynb` from top to bottom. The notebook downloads the UCI Banknote Authentication data on its first run and caches it in the repository root. An internet connection is needed for that first download. If the download fails, download the dataset from the UCI Banknote Authentication repository and save it as `banknote_authentication.csv` in the project root with columns `variance,skewness,curtosis,entropy,class`.

## Assignment coverage
- **Part A:** Gini impurity, entropy, threshold selection, recursive manual decision tree, predictions, 2D boundaries using variance and skewness, manual tree visualization/rules, criterion and depth experiments, Scikit-learn comparison.
- **Part B:** training-only standardization, binary labels mapped to -1/+1, manual linear soft-margin SVM using hinge loss and subgradient descent, separating boundary/margins/violations, Scikit-learn comparison, C/learning-rate/iteration experiments.
- **Part C:** `make_moons` dataset and linear, polynomial, and RBF SVM boundary plots.
- **Part D:** consistent stratified train-test split, all four original features, manual and Scikit-learn trees, manual and Scikit-learn linear SVMs, and RBF SVM; accuracy, precision, recall, F1, training time, and prediction time.

## Observations
The notebook prints measured results for the current run. Use those values when discussing performance: execution times vary by machine and run. Trees are interpretable but may overfit as depth grows. SVMs are sensitive to feature scale, so the scaler is fitted only on training data. Nonlinear kernels, especially RBF, can model curved boundaries that a linear SVM cannot. The from-scratch models make the optimization and splitting logic visible, while Scikit-learn provides optimized reference implementations.

## GitHub submission
The assignment specifies a **public GitHub repository link only**. Before submission:
1. Run all notebook cells from top to bottom.
2. Check that generated plots and comparison CSV files are present in `results/`.
3. Commit the notebook, README, requirements, dataset (if course rules permit), and generated result artifacts.
4. Create a **public** repository and submit only its URL.
