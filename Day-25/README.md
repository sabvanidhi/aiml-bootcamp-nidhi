# California Housing – Linear Model Pipeline

This project is about predicting median house values using the California Housing dataset.

I explored the data, split it into training and test sets, and compared different linear models:

* Linear Regression
* Ridge
* Lasso
* Tuned Lasso Pipeline

I used StandardScaler with the regularized models and 5-fold cross-validation for model comparison and tuning.

## Results

| Model             |  CV R² | Test R² |
| ----------------- | -----: | ------: |
| Baseline          | -0.002 |       — |
| Linear Regression |  0.840 |       — |
| Ridge             |  0.840 |       — |
| Lasso             | -0.002 |       — |
| Final Pipeline    |  0.840 |   0.838 |

The final Lasso Pipeline selected **alpha = 0.001**.

The final model achieved a **Test R² of 0.838**, which is very close to the CV score of 0.840.

## Final Model

I selected the tuned Lasso Pipeline as the final model because it achieved a good CV score after hyperparameter tuning.

The Lasso model was tuned using 5-fold cross-validation. The best alpha was **0.001**.

The tuned model had **0 zero coefficients**, meaning that none of the features were completely removed.

The coefficient chart was used to understand which features had more influence on the predicted house value.

## Files

* `notebook.ipynb` – complete analysis
* `coefficients.png` – coefficient interpretation chart
* `model_comparison.csv` – model comparison results
* `README.md` – project summary

## How to Run

Open `Linear_model_pipeline.ipynb` in Jupyter Notebook and run the cells from top to bottom.
