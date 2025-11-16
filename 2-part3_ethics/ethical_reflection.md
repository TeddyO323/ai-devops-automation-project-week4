# Ethical Reflection: Predictive Model for Issue Priority

## Potential Biases
Even though the Random Forest model performs well on the Kaggle Breast Cancer dataset, several ethical considerations apply when deploying predictive models in a real company context:

1. **Underrepresented Teams or Groups**
   - If certain teams or project types are underrepresented in historical data, the model may systematically assign lower or higher priority incorrectly.
   - This can lead to unfair resource allocation and impact team productivity or morale.

2. **Historical Bias**
   - The model is trained on past priorities, which may have been influenced by human biases or inconsistent prioritization rules.
   - This could reinforce existing inequalities in task assignment or resource allocation.

3. **Feature Bias**
   - Certain features (e.g., “team name,” “department”) could inadvertently encode social or demographic biases.
   - Without careful feature selection or preprocessing, these biases propagate into predictions.

## Fairness Mitigation
To address potential biases, tools like **IBM AI Fairness 360 (AIF360)** can be used:

- **Bias Metrics**
  - Measure disparities in predictions across different groups or teams
  - Detect imbalances in classification outcomes
- **Bias Mitigation Algorithms**
  - Pre-processing: Reweight or balance training data
  - In-processing: Constrain model during training to satisfy fairness criteria
  - Post-processing: Adjust predictions to reduce unfair disparities

## Reflection
AI models can unintentionally perpetuate historical or structural biases. In resource allocation scenarios, even small disparities can accumulate over time and create unfair outcomes. Incorporating fairness assessment and mitigation tools ensures that predictions are both accurate and equitable. Ethical deployment requires continuous monitoring, auditing, and collaboration with stakeholders to identify and correct biases.

