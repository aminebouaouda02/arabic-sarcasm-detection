from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, f1_score


def evaluate_scores(
    y_true: object,
    scores: object,
    threshold: float = 0.5,
) -> dict[str, float]:
    """Calcule les trois métriques demandées par le sujet."""
    y = np.asarray(y_true).astype(int)
    p = np.asarray(scores)
    pred = (p >= threshold).astype(int)
    return {
        "F1 sarcastique": float(f1_score(y, pred, zero_division=0)),
        "PR-AUC": float(average_precision_score(y, p)),
        "Macro-F1": float(f1_score(y, pred, average="macro", zero_division=0)),
    }


def append_result(path: str | Path, row: dict[str, object]) -> None:
    """Ajoute une ligne de résultat dans results.csv."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame([row])
    frame.to_csv(output, mode="a", header=not output.exists(), index=False)


def save_predictions(
    path: str | Path,
    ids: object,
    y_true: object,
    scores: object,
    threshold: float = 0.5,
) -> None:
    """Exporte le format demandé : id, y_true, y_pred, probabilite."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    probabilities = np.asarray(scores, dtype=float)
    pd.DataFrame(
        {
            "id": np.asarray(ids),
            "y_true": np.asarray(y_true).astype(int),
            "y_pred": (probabilities >= threshold).astype(int),
            "probability": probabilities,
        }
    ).to_csv(output, index=False)
