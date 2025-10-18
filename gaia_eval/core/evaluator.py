import re
import math
from typing import Optional, Tuple
from .models import GAIATask, GAIAEvaluationResult


class GAIAEvaluator:
    """
    Evaluator adhering to the official GAIA benchmark quasi-exact match protocol.
    Supports numerical tolerance, comma-separated set matching, and normalized string equality.
    """

    @staticmethod
    def normalize_text(text: str) -> str:
        s = text.strip().lower()
        s = re.sub(r"\b(a|an|the)\b", " ", s)  # Remove English articles
        s = re.sub(r"[^\w\s\.,-]", "", s)      # Remove extra punctuation except decimal/dash
        s = re.sub(r"\s+", " ", s).strip()
        return s

    @staticmethod
    def try_parse_number(text: str) -> Optional[float]:
        cleaned = text.replace(",", "").strip()
        # Extract number if wrapped
        match = re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", cleaned)
        if match:
            try:
                return float(match.group(0))
            except ValueError:
                return None
        return None

    def evaluate(self, task: GAIATask, prediction: str) -> GAIAEvaluationResult:
        pred_norm = self.normalize_text(prediction)
        gt_norm = self.normalize_text(task.ground_truth)

        # 1. Exact or normalized string match
        if pred_norm == gt_norm or task.ground_truth.lower().strip() in prediction.lower().strip():
            return GAIAEvaluationResult(
                task_id=task.task_id,
                level=task.level,
                predicted_answer=prediction,
                ground_truth=task.ground_truth,
                is_correct=True,
                score=1.0,
                notes="Normalized text match"
            )

        # 2. Number comparison
        num_pred = self.try_parse_number(prediction)
        num_gt = self.try_parse_number(task.ground_truth)
        if num_pred is not None and num_gt is not None:
            if math.isclose(num_pred, num_gt, rel_tol=1e-3, abs_tol=1e-3):
                return GAIAEvaluationResult(
                    task_id=task.task_id,
                    level=task.level,
                    predicted_answer=prediction,
                    ground_truth=task.ground_truth,
                    is_correct=True,
                    score=1.0,
                    notes="Numerical value match within tolerance"
                )

        # 3. Comma-separated set matching (unordered items)
        if "," in task.ground_truth:
            gt_items = set(i.strip() for i in gt_norm.split(",") if i.strip())
            pred_items = set(i.strip() for i in pred_norm.split(",") if i.strip())
            if gt_items and gt_items == pred_items:
                return GAIAEvaluationResult(
                    task_id=task.task_id,
                    level=task.level,
                    predicted_answer=prediction,
                    ground_truth=task.ground_truth,
                    is_correct=True,
                    score=1.0,
                    notes="Set element equivalence"
                )

        return GAIAEvaluationResult(
            task_id=task.task_id,
            level=task.level,
            predicted_answer=prediction,
            ground_truth=task.ground_truth,
            is_correct=False,
            score=0.0,
            notes=f"Mismatch: '{prediction}' != '{task.ground_truth}'"
        )
