# Day27 Model Memo

## 1. Objective

The objective was to predict Titanic passenger survival using 891 passenger records. The model used six features: `pclass`, `sex_male`, `age`, `sibsp`, `parch`, and `fare`. Missing age values were filled using the median within passenger class and sex groups, with the overall age median used for any remaining missing values. Missing fare values were filled using the overall median.

## 2. Model Choice

Random Forest is a suitable baseline because it combines multiple decision trees, reducing the instability of a single tree. It can capture nonlinear relationships and interactions without requiring feature scaling. Bootstrap sampling allows individual trees to train on different samples, while out-of-bag (OOB) evaluation provides an estimate of performance using training observations left out of each tree's bootstrap sample.

## 3. Evaluation

The selected model uses 100 trees with `max_features=0.5`. Its OOB score is 0.8048, test accuracy is 0.8045, and test ROC-AUC is 0.8891.

The OOB score and test accuracy differ by approximately 0.0003, indicating that these two performance estimates are very close for this experiment. However, this does not guarantee that the model will perform equally well on new datasets.

In a 25-bootstrap stability experiment, the 200-tree Random Forest achieved a mean ROC-AUC of 0.8765 with a standard deviation of 0.0177. This suggests relatively stable performance across the different bootstrap training samples tested.

## 4. Key Findings

**Sex:** `sex_male` was the most important feature according to permutation importance, with a score of 0.1777. Its partial dependence plot (PDP) showed that predicted survival probability generally decreases when `sex_male` changes from 0 (female) to 1 (male).

**Fare:** `fare` had a permutation importance score of 0.0513. Its PDP showed a generally positive relationship, meaning that the model generally predicts higher survival probabilities at higher fares, although the relationship includes fluctuations.

These findings describe the model's learned relationships and do not establish causal effects.

**Random noise:** The artificial `random_noise` feature ranked 3rd in impurity importance, with a score of 0.1994, but ranked 6th in permutation importance, with a score of 0.0081. This illustrates why impurity importance can overstate the importance of features that do not provide reliable predictive information.

## 5. Risks and Limitations

- **Small dataset:** The 891 passenger records may not represent all populations, and performance can vary across data splits.
- **Correlation is not causation:** PDPs describe the model's predictions, not real-world causal effects.
- **Feature importance limitations:** Impurity importance can assign misleadingly high importance to uninformative features, as demonstrated by `random_noise`.
- **Missing values:** Median imputation can introduce uncertainty and may hide meaningful differences between passengers.
- **Performance uncertainty:** Similar OOB and test accuracy values do not guarantee future performance.
- **Fairness considerations:** The model uses sex as a predictor, and historical Titanic survival patterns should not automatically be generalized to modern populations.
- **Evaluation procedure:** The notebook compares several models using test-set results before evaluating the selected model again. A stricter procedure would select the model using training data and OOB results, then evaluate the test set only once.

## 6. Recommendation

Use this Random Forest as a baseline and compare it with Logistic Regression and Gradient Boosting using cross-validation. Evaluate whether the Random Forest's ability to capture nonlinear relationships provides a meaningful improvement over simpler and alternative models. Keep the test set separate during model selection and use it only for the final evaluation.