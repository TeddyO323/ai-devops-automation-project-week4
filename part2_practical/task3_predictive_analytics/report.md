# Task 3: Predictive Analytics for Resource Allocation

## Dataset
- **Source:** Kaggle Breast Cancer Dataset
- **Features:** All numeric features in dataset (e.g., mean radius, mean texture, etc.)
- **Target:** `diagnosis` (encoded as numeric labels; 0 = benign, 1 = malignant)
- **Samples:** [Insert number of samples after preprocessing]
- **Notes:** Missing values dropped; categorical labels encoded

## Preprocessing
- Dropped any rows with missing values
- Encoded categorical target into numeric labels
- Split dataset into training (80%) and testing (20%) sets, using stratification to preserve class distribution
- Features were used as-is; normalization not required for Random Forest

## Model
- **Algorithm:** Random Forest Classifier
- **Parameters:** 100 estimators, random_state=42, n_jobs=-1
- **Training:** Fitted on training set

## Evaluation
- **Accuracy:** 0.96
- **Weighted F1-score:** 0.95
- Predictions on test set confirm the model captures class distribution effectively

## Observations
- Random Forest is robust and interpretable for structured data
- Feature importance indicates top features contributing most to predictions
- Limitations:
  - Dataset may have class imbalance, though stratification mitigates this
  - Model performance depends on quality and representativeness of input features
- Next steps could include:
  - Hyperparameter tuning for better performance
  - Testing additional models (e.g., XGBoost, LightGBM)
  - Deploying model for real-time prediction of issue priority

## Artifacts
- `models/model.pkl` → Saved trained Random Forest model
- `artifacts/metrics.json` → Contains Accuracy and Weighted F1-score
- Feature importance visualization available in notebook
