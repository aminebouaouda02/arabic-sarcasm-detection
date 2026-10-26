import numpy as np

from src.models.metrics import evaluate_scores
from src.preprocess.text import clean_text, remove_sarcasm_cues
from src.train.reproducibility import set_seed


def test_metrics_have_required_keys():
    result = evaluate_scores([0, 1], [0.1, 0.9])
    assert set(result) == {"F1 sarcastique", "PR-AUC", "Macro-F1"}


def test_preprocessing_keeps_content():
    assert clean_text("  نص   ساخر  ") == "نص ساخر"
    assert "URL" in remove_sarcasm_cues("tweet https://example.org")


def test_seed_is_reproducible():
    set_seed(42)
    first = np.random.random()
    set_seed(42)
    assert first == np.random.random()
