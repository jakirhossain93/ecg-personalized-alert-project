# Project Report

## Personalized ECG Alert Prioritization
### A Patient-Specific Baseline Experiment on Ambulatory ECG

## 1. Project Objective
This project investigates whether patient-specific ECG features can improve
the prioritization of ventricular ectopic events compared with a global model.

## 2. Dataset
The project uses the MIT-BIH Arrhythmia Database available through PhysioNet.

Beat annotations are grouped into:
- Normal-like: N, L, R, e, j
- Ventricular ectopic: V, E

## 3. Features
The global model uses:
- Previous RR interval
- Next RR interval
- ECG amplitude range
- Signal standard deviation
- Signal energy

The personalized model additionally uses patient-specific RR features:
- Previous RR ratio
- Next RR ratio
- Previous RR deviation
- Next RR deviation

## 4. Modeling
Random Forest classifiers are used to compare:
1. Global ECG classification
2. Personalized baseline ECG classification

Record-level train/test separation is used to reduce data leakage.

## 5. Alert Prioritization
Personalized model probabilities are converted into experimental alert levels:

- Low: < 0.35
- Moderate: 0.35 to < 0.60
- High: 0.60 to < 0.85
- Urgent: >= 0.85

These thresholds are experimental and are not intended for clinical use.

## 6. Evaluation
Model performance is evaluated using:
- Accuracy
- Precision
- Recall
- F1 score
- ROC-AUC
- PR-AUC
- Confusion matrix

## 7. Purpose and Limitations
This project is a research and educational experiment. It does not provide
medical diagnosis or clinical recommendations. Further validation on
independent ambulatory ECG datasets would be required before any clinical use.
