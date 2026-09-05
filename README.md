# Personalized ECG Alert Prioritization

## A Patient-Specific Baseline Experiment on Ambulatory ECG

This project investigates whether patient-specific ECG features can improve ventricular ectopic beat detection and support probability-based alert prioritization for ambulatory ECG monitoring.

## Dataset

The experiment uses the MIT-BIH Arrhythmia Database from PhysioNet.

Beat annotations were grouped into two classes:

- Normal-like beats: N, L, R, e, j
- Ventricular ectopic beats: V, E

## Approach

Two Random Forest classifiers were compared:

1. Global Model - uses ECG morphology and RR-interval features.
2. Personalized Model - adds patient-specific baseline features representing deviations from an individual's typical rhythm.

A record-level train/test split was used to reduce patient-level data leakage.

## Final Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | PR-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Global | 0.9300 | 0.6671 | 0.9938 | 0.7983 | 0.9986 | 0.9942 |
| Personalized | 0.9558 | 0.8036 | 0.9033 | 0.8506 | 0.9840 | 0.9315 |

### Global Model Confusion Matrix

- True negatives: 9,158
- False positives: 800
- False negatives: 10
- True positives: 1,603

### Personalized Model Confusion Matrix

- True negatives: 9,602
- False positives: 356
- False negatives: 156
- True positives: 1,457

The personalized model improved accuracy, precision, and F1 score while substantially reducing false positives.

The global model achieved higher recall, ROC-AUC, and PR-AUC.

## Alert Prioritization

Personalized-model probabilities were mapped into experimental alert-priority levels:

- Low: < 0.35
- Moderate: 0.35-0.60
- High: 0.60-0.85
- Urgent: >= 0.85

Final alert distribution:

| Alert Level | Number of Beats |
|---|---:|
| Low | 8,857 |
| Moderate | 1,193 |
| High | 376 |
| Urgent | 1,145 |

These thresholds are research-defined experimental categories and are not clinical decision thresholds.

## Project Folders

- results/ - model metrics, predictions, and alert summary
- figures/ - ROC, PR, confusion matrices, and alert distribution
- notebooks/ - experiment notebook
- src/ - reusable project code
- tests/ - project tests
- docs/ - project documentation

## Research Scope

This project is an educational and research experiment. It is not intended for clinical diagnosis, treatment, or real-world medical decision-making.
