from pathlib import Path

import pandas as pd


def read_results(path: str | Path = "results/results.csv") -> pd.DataFrame:
    """Lit les résultats réellement produits par les notebooks."""
    output = Path(path)
    if not output.exists():
        return pd.DataFrame()
    return pd.read_csv(output)
