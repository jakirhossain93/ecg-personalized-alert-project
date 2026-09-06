
"""
Model-building utilities for the Personalized ECG Alert project.
"""

from sklearn.ensemble import RandomForestClassifier


def build_random_forest(random_state=42):
    """
    Create the Random Forest classifier used in the experiment.
    """
    model = RandomForestClassifier(
        n_estimators=300,
        random_state=random_state,
        class_weight="balanced",
        n_jobs=-1
    )

    return model


def train_model(X_train, y_train, random_state=42):
    """
    Train and return a Random Forest classifier.
    """
    model = build_random_forest(
        random_state=random_state
    )

    model.fit(
        X_train,
        y_train
    )

    return model


def predict_model(model, X):
    """
    Return class predictions and positive-class probabilities.
    """
    predictions = model.predict(X)

    probabilities = model.predict_proba(X)[:, 1]

    return predictions, probabilities
