## Business Recommendation

The fraud detection system is designed to help the claims team **prioritize claims for investigation**. It does not automatically classify a claim as fraudulent; instead, it assigns a fraud-risk probability so investigators can focus their limited review capacity on higher-risk claims.

### Model Performance

The selected model is an **XGBoost classifier**. On the held-out test data, it achieved:

- **ROC-AUC:** 0.766
- **PR-AUC:** 0.166
- **Fraud prevalence:** 3.7%

The PR-AUC is substantially higher than the random baseline of approximately 0.037, indicating that the model provides useful fraud-risk separation despite the highly imbalanced dataset.

### Recommended Threshold

Using the business costs:

- **False Positive (FP) cost:** 1
- **False Negative (FN) cost:** 20
- **Investigation capacity:** 200 claims

The unconstrained cost-optimal threshold was **0.04**, with a total cost of **1028**. However, it flagged **388 claims**, exceeding the investigation capacity.

Therefore, the final recommended threshold is **0.09**:

- **Claims flagged:** 179
- **Total cost:** 1113
- **Default threshold (0.50) cost:** 1426
- **Cost saving:** 313 (**22.0%**)

This threshold keeps the investigation workload within the 200-claim capacity while reducing the estimated business cost compared with the default 0.50 threshold.

### Key Fraud Drivers

SHAP analysis identified the following important factors:

- **Claim amount:** higher amounts generally increase predicted fraud risk.
- **Prior claims:** more previous claims generally increase predicted risk.
- **Days to report:** longer reporting delays generally increase predicted risk.
- **Customer tenure:** longer tenure generally tends to reduce predicted risk.
- **Age, channel, and policy type:** also contribute to the model's predictions.

These factors are broadly consistent with common fraud-investigation signals, but SHAP describes patterns learned by the model and does not establish causation.

### Probability Calibration

Calibration was evaluated because the system uses predicted probabilities for cost-based threshold decisions.

- **Brier score before calibration:** 0.03496
- **Brier score after calibration:** 0.03366

The lower calibrated Brier score indicates improved probability reliability. Calibration should be performed using data that maintains the **real-world class balance**, rather than resampled data.

### Limitations

1. The model will still produce **false positives and false negatives**. The selected threshold balances investigation capacity and business cost rather than detecting every fraudulent claim.

2. **Fraud patterns can change over time.** Model performance and the selected threshold should therefore be monitored and periodically revalidated using newer claims data.

### Next Steps

With additional development time, the next steps would be:

- Validate the model and threshold on newer/future claims.
- Review false positives and missed fraud cases with claims investigators.
- Monitor investigation workload and fraud detection performance.
- Continue monitoring probability calibration.
- Reassess the threshold when fraud patterns, costs, or investigation capacity change.

### Final Recommendation

Use the **XGBoost model with a 0.09 threshold** as a claims-screening and prioritization tool under the current cost assumptions and 200-claim investigation capacity. Final fraud decisions should remain with the claims investigation team.