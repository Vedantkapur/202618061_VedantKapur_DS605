# DS605 Lab Assignment 7 — Eigenfaces and Face Recognition

## Files
- `DS605_Lab7_Eigenfaces.ipynb`: Complete notebook for Parts A–D.
- `requirements.txt`: Python dependencies.

## Dataset setup
This project uses the AT&T Database of Faces (ORL). Obtain the dataset from the source provided by your instructor or the official dataset mirror, extract it, and place the subject folders (`s1`, `s2`, ... or equivalent) under a local folder such as `att_faces/`.

Update `DATASET_DIR` near the top of the notebook to point to the directory containing the subject folders. The notebook supports `.pgm`, `.png`, `.jpg`, `.jpeg`, `.bmp`, `.tif`, and `.tiff` images.

## Run
```bash
python -m pip install -r requirements.txt
jupyter notebook DS605_Lab7_Eigenfaces.ipynb
```
Run every cell from top to bottom. The notebook produces:
- Image samples and pixel intensity distribution
- Stratified train/test split
- NumPy eigendecomposition and SVD PCA comparison
- Cumulative explained-variance plot and eigenfaces
- Reconstruction examples and error metrics
- Approximate raw-vs-PCA storage comparison
- Raw-pixel and PCA nearest-neighbour recognition
- KNN and SVM classifier comparison and component-count sweep

## Important academic requirement
PCA/eigenface calculations use NumPy linear-algebra operations rather than `sklearn.decomposition.PCA`. Scikit-learn is used only for the traditional machine-learning classifier comparison.

## Results
Accuracy, selected component count, reconstruction error, and storage figures are computed when the notebook is run on the dataset. They are intentionally not hard-coded because they depend on the exact dataset layout and execution environment.
