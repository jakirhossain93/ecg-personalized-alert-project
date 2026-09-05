
"""
Main experiment runner for the Personalized ECG Alert Project.

This module connects:
- data loading
- feature engineering
- model training
- evaluation
- alert prioritization

Research/educational use only.
"""

from data_pipeline import extract_beats
from features import (
    add_personalized_features,
    get_global_feature_columns,
    get_personalized_feature_columns
)
from modeling import train_model, predict_model
from evaluation import evaluate_model
from alerting import assign_alert_levels, summarize_alerts


def run_single_record_demo(record_name="100"):
    """
    Run a small demonstration using one MIT-BIH record.

    This function is intended as a reproducibility example,
    not as the final record-level train/test experiment.
    """

    data = extract_beats(record_name)

    if data.empty:
        raise ValueError(
            f"No eligible beats extracted from record {record_name}."
        )

    data = add_personalized_features(data)

    print(f"Record: {record_name}")
    print(f"Extracted beats: {len(data)}")
    print("Global features:")
    print(get_global_feature_columns())
    print("Personalized features:")
    print(get_personalized_feature_columns())

    return data


if _name_ == "_main_":
    demo_data = run_single_record_demo("100")
    print("\nDemo completed successfully.")
