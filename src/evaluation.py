
"""
Evaluation utilities for the Personalized ECG Alert project.
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    average_precision_score,
    confusion_matrix
)


def evaluate_model(y_true, y_pred, y_prob):
    """
    Calculate classification performance metrics.
    """
    metrics = {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(
            y_true, y_pred, zero_division=0
        ),
        "Recall": recall_score(
            y_true, y_pred, zero_division=0
        ),
        "F1": f1_score(
            y_true, y_pred, zero_division=0
        ),
        "ROC_AUC": roc_auc_score(
            y_true, y_prob
        ),
        "PR_AUC": average_precision_score(
            y_true, y_prob
        )
    }

    return metrics


def get_confusion_matrix(y_true, y_pred):
    """
    Return the binary classification confusion matrix.
    """
    return confusion_matrix(y_true, y_pred)
