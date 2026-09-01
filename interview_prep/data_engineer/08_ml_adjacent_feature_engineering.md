# ML-adjacent Data Engineering and Feature Engineering - questions and answers

## 1. What does ML-adjacent mean for a Data Engineer?

It means supporting machine-learning workflows without necessarily owning all modeling decisions. This includes data preparation, feature pipelines, training datasets, batch scoring, monitoring, reproducibility, and production deployment support.

## 2. What is feature engineering?

Feature engineering is the process of creating input variables for a model from raw data. Good features capture useful patterns while avoiding leakage and preserving the time context of prediction.

## 3. What is data leakage?

Data leakage happens when the model uses information that would not be available at prediction time. It can make evaluation results look unrealistically good and fail in production.

## 4. Example of leakage in credit risk

If a model predicts default at application time but uses variables created after repayment behavior is known, that is leakage. For example, using “days late after loan approval” to predict default at the moment of application.

## 5. How would you avoid leakage?

I would define the prediction timestamp, include only data available before that timestamp, use temporal train/test splits, review feature logic with domain experts, and test whether suspicious features are proxies for the target.

## 6. What is a temporal train/test split?

A temporal split trains on earlier periods and tests on later periods. It is often better for real-world prediction because production data arrives over time.

## 7. What is model stability?

Model stability means performance and behavior remain reasonably consistent over time and across data segments. Instability can come from data drift, concept drift, poor features, or changing business processes.

## 8. What is data drift?

Data drift means the distribution of input data changes over time. For example, applicant income, transaction volume, or device type distribution may shift.

## 9. What is concept drift?

Concept drift means the relationship between features and target changes over time. For example, the meaning of a risk signal can change after a policy or market change.

## 10. What metrics would you use for default classification?

Common metrics include ROC-AUC, PR-AUC, precision, recall, F1, confusion matrix, calibration, and business metrics such as approval rate, default rate, and expected loss.

## 11. Why can accuracy be a bad metric for default prediction?

Default datasets are often imbalanced. If only 5% of customers default, a model that always predicts “no default” can achieve 95% accuracy but has no business value.

## 12. What is XGBoost?

XGBoost is a gradient-boosted decision tree library commonly used for structured/tabular data. It can model nonlinear relationships and interactions and is often strong for risk and classification problems.

## 13. How would you put a model into production?

I would define the scoring mode, package the model and preprocessing, version the model and features, create a batch or real-time scoring pipeline, monitor inputs and outputs, log predictions, and set rollback procedures.

## 14. What is reproducibility in ML?

Reproducibility means being able to recreate the training data, features, model version, parameters, and evaluation results. This requires versioned code, data snapshots or clear data ranges, and controlled environments.

## 15. How would you collaborate with data scientists?

I would clarify feature definitions, data availability, freshness, training windows, validation rules, production constraints, and monitoring requirements. Data engineering ensures that model inputs are reliable and repeatable.

## 16. How would you explain your experience at MO Technologies?

I built business-facing ML workflows on AWS warehouse data, including data preparation, feature engineering, evaluation, and model training with scikit-learn and XGBoost. I also supported continuous model iteration and production deployment, helping reduce default rate while improving stability.

## 17. How do you validate features before training?

I would check missing values, distributions, outliers, data types, uniqueness, time availability, leakage risk, correlation with target, and stability across time periods.

## 18. What is target leakage through aggregations?

It happens when an aggregate feature accidentally includes future data. For example, calculating customer default rate using the full dataset instead of only data available before the prediction date.

## 19. How would you design daily batch scoring?

A daily Airflow DAG could extract eligible entities, compute features as of the scoring date, load the model version, generate predictions, validate output, write scores to a production table, and notify downstream consumers.

## 20. Trick question: do more features always improve the model?

No. More features can add noise, leakage, complexity, instability, and maintenance cost. Good feature engineering prioritizes predictive value, reliability, interpretability, and production feasibility.
