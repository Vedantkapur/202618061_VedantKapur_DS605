# DS605 Lab 6 — Feature Extraction and Machine Learning with Image and Text Data

## Assignment
**DS605: Fundamentals of Machine Learning — Lab Assignment 6**

The assignment uses:
- Asphalt Crack Dataset — 400 images
- Email Spam Classification Dataset — 5,172 emails

The required workflow is:

`Raw Image/Text -> Preprocessing -> Feature Extraction / Vectorization -> Train-Test Split -> ML Model -> Evaluation -> Representation Improvement`
--------------------------------------------
StudentName: Vedant Kapur

Student Id: 202618061
---------------------------------------------


## Repository structure

```text
DS605_Lab6/
├── DS605_Lab6.ipynb
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── images/
│   │   ├── crack/
│   │   └── non-crack/
│   └── text/
│       └── email_spam.csv
└── outputs/
    ├── image_visualizations/
    ├── tables/
    └── figures/
```

## 1. Dataset setup

Download the datasets named in the assignment from their original sources and place them under the `data/` directories.

### Image dataset
The notebook can identify labels from:
- parent folders named `crack` and `non-crack`, or
- filenames containing `crack` / `non-crack`.

If your image dataset uses a different naming convention, edit `infer_image_label()` in the notebook.

### Text dataset
Put the email CSV under `data/text/`.

The notebook automatically searches for common text/label column names such as:
- text / email text / message / body / content
- label / category / class / spam / email type / target

If automatic detection fails, set `text_col` and `label_col` manually.

## 2. Installation

```bash
pip install -r requirements.txt
```

Recommended Python version: **3.10+**

## 3. Run

Open:

```text
DS605_Lab6.ipynb
```

Run all cells from top to bottom.

The notebook generates:
- extracted image feature table
- sample grayscale + Canny visualization
- image classifier results
- CountVectorizer vs TF-IDF comparison
- improved text representation results
- CSV files containing the numerical results

## Part A — Image

The image pipeline:
1. Reads images with PIL.
2. Converts RGB images to grayscale.
3. Resizes every image to 128 × 128.
4. Extracts numerical intensity features using NumPy:
   - mean brightness
   - standard deviation / contrast
   - median intensity
   - minimum and maximum intensity
   - dark-pixel ratio
   - bright-pixel ratio
   - intensity IQR
5. Uses OpenCV Canny edge detection.
6. Extracts edge count and edge density.
7. Trains:
   - Logistic Regression
   - Random Forest
8. Reports:
   - accuracy
   - precision
   - recall
   - F1-score
   - confusion matrix
   - training time
   - prediction time

The extracted table is saved to:

```text
outputs/tables/image_features.csv
```

## Part B — Text

The text pipeline:
1. Loads the email CSV.
2. Checks the spam/non-spam distribution.
3. Performs basic cleaning:
   - lowercase
   - URL replacement
   - removal of non-alphanumeric punctuation
   - whitespace normalization
4. Creates:
   - CountVectorizer features
   - TF-IDF features
5. Trains Logistic Regression on both representations.
6. Compares:
   - number of features
   - accuracy
   - precision
   - recall
   - F1-score
   - vectorization time
   - training time
   - prediction time

Results are saved to:

```text
outputs/tables/text_vectorization_results.csv
```

## Part C — Representation improvement

Two representation improvements are included.

### Image improvement
The notebook changes Canny thresholds and normalizes grayscale intensity before extracting a compact representation.

### Text improvement
The notebook uses:

```python
TfidfVectorizer(
    ngram_range=(1, 2),
    max_features=20000,
    min_df=2,
    sublinear_tf=True
)
```

This introduces word bigrams while bounding vocabulary size.

The improved results are saved in:

```text
outputs/tables/image_improved_results.csv
outputs/tables/text_improved_results.csv
```

## Important: do not invent results

The final accuracy, precision, recall, F1, feature counts, and timing values depend on the exact dataset files and machine on which the notebook is run.

Therefore, run the notebook first and use the generated CSV files for the final GitHub report. Do not manually type fabricated scores into the README.

## Observations to report

After running the notebook, discuss:

1. How brightness, contrast, dark/bright pixel ratios, and edge density differ between crack and non-crack images.
2. Whether Logistic Regression or Random Forest better captured the image-feature relationships on the supplied split.
3. Whether CountVectorizer or TF-IDF produced more useful predictive features.
4. The relationship between feature dimensionality and training/vectorization time.
5. Whether the improved TF-IDF representation changed accuracy/F1 and how its vocabulary size changed.
6. The trade-off between richer representations, computation, and predictive performance.

## GitHub submission

The assignment requests a **public GitHub repository link only**.

Before submitting:
1. Run the entire notebook.
2. Confirm that all output tables and visualizations are generated.
3. Add the required sample image/Canny visualization.
4. Confirm the README contains the actual observed results and observations.
5. Push the repository publicly.
6. Submit only the repository URL.

