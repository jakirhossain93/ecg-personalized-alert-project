
"""
Feature engineering utilities for the Personalized ECG Alert project.

Includes patient/record-specific RR baseline features.
"""

import numpy as np
import pandas as pd


def add_personalized_features(df):
    """
    Add record-specific RR baseline features.

    For each ECG record, the median RR interval is used as
    the patient's baseline rhythm estimate.
    """
    data = df.copy()

    # Record-specific median RR baseline
    median_rr = data.groupby("record")["prev_rr"].transform("median")

    # Avoid division by zero
    median_rr = median_rr.replace(0, np.nan)

    # Personalized RR ratios
    data["prev_rr_ratio"] = data["prev_rr"] / median_rr
    data["next_rr_ratio"] = data["next_rr"] / median_rr

    # Absolute deviation from the record-specific baseline
    data["prev_rr_deviation"] = np.abs(
        data["prev_rr"] - median_rr
    )

    data["next_rr_deviation"] = np.abs(
        data["next_rr"] - median_rr
    )

    return data


def get_global_feature_columns():
    """Features used by the global ECG model."""
    return [
        "prev_rr",
        "next_rr",
        "amplitude_range",
        "signal_std",
        "signal_energy"
    ]


def get_personalized_feature_columns():
    """Features used by the personalized ECG model."""
    return get_global_feature_columns() + [
        "prev_rr_ratio",
        "next_rr_ratio",
        "prev_rr_deviation",
        "next_rr_deviation"
    ]
