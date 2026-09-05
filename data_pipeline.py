
"""
ECG data loading and beat extraction utilities.

Dataset:
MIT-BIH Arrhythmia Database (PhysioNet)
"""

import wfdb
import numpy as np
import pandas as pd


NORMAL_LIKE = {"N", "L", "R", "e", "j"}
VENTRICULAR = {"V", "E"}


def load_record(record_name, pn_dir="mitdb"):
    """Load an ECG record and its beat annotations."""
    record = wfdb.rdrecord(record_name, pn_dir=pn_dir)
    annotation = wfdb.rdann(record_name, "atr", pn_dir=pn_dir)
    return record, annotation


def extract_beats(record_name, pn_dir="mitdb"):
    """
    Extract labeled beats and basic RR/morphology information
    from one MIT-BIH ECG record.
    """
    record, annotation = load_record(record_name, pn_dir)

    signal = record.p_signal[:, 0]
    fs = record.fs

    samples = annotation.sample
    symbols = annotation.symbol

    rows = []

    for i in range(1, len(samples) - 1):
        sample = samples[i]
        symbol = symbols[i]

        if symbol not in NORMAL_LIKE and symbol not in VENTRICULAR:
            continue

        if sample - 100 < 0 or sample + 100 >= len(signal):
            continue

        prev_rr = (samples[i] - samples[i - 1]) / fs
        next_rr = (samples[i + 1] - samples[i]) / fs

        segment = signal[sample - 100:sample + 100]

        label = 1 if symbol in VENTRICULAR else 0

        rows.append({
            "record": record_name,
            "sample": sample,
            "symbol": symbol,
            "label": label,
            "prev_rr": prev_rr,
            "next_rr": next_rr,
            "amplitude_range": np.ptp(segment),
            "signal_std": np.std(segment),
            "signal_energy": np.mean(segment ** 2)
        })

    return pd.DataFrame(rows)
