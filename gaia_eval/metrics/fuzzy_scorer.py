from typing import Tuple


def token_f1_score(prediction: str, ground_truth: str) -> float:
    """
    Computes token-level precision, recall, and F1 score between prediction and ground truth.
    """
    pred_tokens = prediction.strip().lower().split()
    truth_tokens = ground_truth.strip().lower().split()

    if not pred_tokens or not truth_tokens:
        return 1.0 if pred_tokens == truth_tokens else 0.0

    common = set(pred_tokens) & set(truth_tokens)
    if not common:
        return 0.0

    precision = len(common) / len(pred_tokens)
    recall = len(common) / len(truth_tokens)
    return round(2.0 * (precision * recall) / (precision + recall), 4)


def levenshtein_similarity(s1: str, s2: str) -> float:
    """
    Calculates normalized Levenshtein similarity ratio between two strings in [0.0, 1.0].
    """
    m, n = len(s1), len(s2)
    if m == 0 and n == 0:
        return 1.0
    if m == 0 or n == 0:
        return 0.0

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # deletion
                dp[i][j - 1] + 1,      # insertion
                dp[i - 1][j - 1] + cost # substitution
            )

    dist = dp[m][n]
    max_len = max(m, n)
    return round(1.0 - (dist / max_len), 4)
