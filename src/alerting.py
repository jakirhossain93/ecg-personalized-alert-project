
"""
Experimental ECG alert-priority utilities.

These thresholds are research-defined categories only.
They are NOT clinical decision thresholds.
"""

import numpy as np
import pandas as pd


ALERT_BINS = [-np.inf, 0.35, 0.60, 0.85, np.inf]
ALERT_LABELS = ["Low", "Moderate", "High", "Urgent"]


def assign_alert_levels(probabilities):
    """
    Convert model probabilities into experimental alert levels.

    Low:      < 0.35
    Moderate: 0.35 to < 0.60
    High:     0.60 to < 0.85
    Urgent:   >= 0.85
    """
    return pd.cut(
        probabilities,
        bins=ALERT_BINS,
        labels=ALERT_LABELS,
        right=False
    )


def summarize_alerts(alert_levels):
    """Return the number of observations in each alert category."""
    series = pd.Series(alert_levels)

    return (
        series.value_counts()
        .reindex(ALERT_LABELS, fill_value=0)
        .rename_axis("Alert_Level")
        .reset_index(name="Count")
    )
