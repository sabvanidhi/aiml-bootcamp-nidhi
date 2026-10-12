# California Housing – Linear Model Pipeline

## Project Overview

This project predicts median house values using the California Housing dataset.

The dataset contains 5,000 rows, eight input features, and one target column: `MedHouseVal`.

I explored the dataset, checked for missing values, and split the data into training and test sets. I compared the following models:

- Dummy Regressor (baseline)
- Linear Regression
- Ridge Regression
- Lasso Regression
- Tuned Lasso Pipeline

I used `StandardScaler` with the regularized models and 5-fold cross-validation to compare models and tune the Lasso regularization parameter.

## Results

| Model | CV R² | Test R² |
|---|---:|---:|
| Baseline | -0.002 | Not evaluated |
| Linear Regression | 0.840 | Not evaluated |
| Ridge | 0.840 | Not evaluated |
| Lasso (default alpha) | -0.002 | Not evaluated |
| Final Lasso Pipeline | 0.840 | 0.838 |

The final pipeline selected **alpha = 0.001** using Lasso cross-validation.

The final model achieved a test R² score of **0.838**, close to its cross-validation R² score of **0.840**.

## Final Model

I selected the tuned Lasso Pipeline as the final model because it achieved a strong cross-validation score after hyperparameter tuning.

The pipeline combines `StandardScaler` and `LassoCV`. This allows feature scaling and model training to be handled together.

The selected alpha was `0.001`. The model had **zero coefficients equal to zero**, meaning none of the eight input features were removed by Lasso at the selected alpha.

The coefficient chart helps interpret the direction and relative size of each feature's contribution to the predictions.

## Files

- `Linear_model_pipeline.ipynb` – complete data analysis, model training, comparison, and evaluation
- `coefficients.png` – coefficient interpretation chart
- `model_comparison.csv` – model comparison results
- `README.md` – project summary

## How to Run

1. Keep `Linear_model_pipeline.ipynb` and `california_housing.csv` in the appropriate project directory.
2. Open `Linear_model_pipeline.ipynb` in Jupyter Notebook.
3. Make sure the required Python libraries are installed, including pandas, matplotlib, and scikit-learn.
4. Run the notebook cells from top to bottom.

The notebook generates the coefficient chart and saves the model comparison results as a CSV file.