from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


BASE_URL = (
    "https://raw.githubusercontent.com/iabufarha/ArSarcasm-v2/main/"
    "ArSarcasm-v2/"
)


def load_data(base_url: str = BASE_URL) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Charge le train et le test officiels d'ArSarcasm-v2."""
    train = pd.read_csv(f"{base_url}training_data.csv")
    test = pd.read_csv(f"{base_url}testing_data.csv")
    train.insert(0, "id", range(len(train)))
    test.insert(0, "id", range(len(test)))
    return train, test


def split_train_validation(
    train: pd.DataFrame,
    random_state: int = 42,
    validation_size: float = 0.10,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Applique le split stratifié imposé par le sujet."""
    return train_test_split(
        train,
        test_size=validation_size,
        random_state=random_state,
        stratify=train["sarcasm"],
    )
