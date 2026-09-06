
"""
Basic tests for the Personalized ECG Alert Project.
"""

import os
import sys
import numpy as np
import pandas as pd

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

SRC = os.path.join(PROJECT_ROOT, "src")

if SRC not in sys.path:
    sys.path.insert(0, SRC)

from alerting import assign_alert_levels, summarize_alerts
from features import (
    add_personalized_features,
    get_global_feature_columns,
    get_personalized_feature_columns
)


def test_alert_assignment():
    probabilities = np.array([0.10, 0.40, 0.70, 0.90])

    levels = assign_alert_levels(probabilities)

    assert list(levels.astype(str)) == [
        "Low",
        "Moderate",
        "High",
        "Urgent"
    ]


def test_alert_summary():
    probabilities = np.array([0.10, 0.20, 0.40, 0.70, 0.90])

    levels = assign_alert_levels(probabilities)
    summary = summarize_alerts(levels)

    assert summary["Count"].sum() == 5

    assert set(summary["Alert_Level"]) == {
        "Low",
        "Moderate",
        "High",
        "Urgent"
    }


def test_feature_lists():
    global_features = get_global_feature_columns()
    personalized_features = get_personalized_feature_columns()

    assert len(global_features) > 0
    assert len(personalized_features) > len(global_features)


def test_personalized_features():
    data = pd.DataFrame({
        "record": ["100", "100", "100"],
        "prev_rr": [0.80, 0.82, 0.78],
        "next_rr": [0.81, 0.79, 0.83],
        "amplitude_range": [1.0, 1.1, 0.9],
        "signal_std": [0.20, 0.22, 0.19],
        "signal_energy": [0.10, 0.12, 0.09]
    })

    result = add_personalized_features(data)

    required = [
        "prev_rr_ratio",
        "next_rr_ratio",
        "prev_rr_deviation",
        "next_rr_deviation"
    ]

    for column in required:
        assert column in result.columns
