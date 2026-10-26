import re

import pandas as pd


def clean_text(value: object) -> str:
    """Normalise seulement les espaces et conserve les indices du sarcasme."""
    if pd.isna(value):
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def remove_sarcasm_cues(text: str) -> str:
    """Retire les URLs, mentions, hashtags et ponctuation pour l'ablation."""
    text = re.sub(r"https?://\S+|www\.\S+", " URL ", text)
    text = re.sub(r"[@#]\S+", " TOKEN ", text)
    return re.sub(r"[!?؟]+", " PUNCT ", text)
