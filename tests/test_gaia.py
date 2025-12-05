from gaia_eval.core.models import GAIATask, GAIALevel, Modality
from gaia_eval.core.evaluator import GAIAEvaluator


def test_gaia_numerical_tolerance():
    evaluator = GAIAEvaluator()
    task = GAIATask(
        task_id="t_num",
        question="What is the result?",
        level=GAIALevel.LEVEL_1,
        modalities=[Modality.TEXT],
        ground_truth="105.25"
    )
    res = evaluator.evaluate(task, "The estimated amount is 105.253 dollars.")
    assert res.is_correct is True


def test_gaia_set_matching():
    evaluator = GAIAEvaluator()
    task = GAIATask(
        task_id="t_set",
        question="List cities",
        level=GAIALevel.LEVEL_2,
        modalities=[Modality.TEXT],
        ground_truth="London, Paris, Berlin"
    )
    res = evaluator.evaluate(task, "Berlin, London, Paris")
    assert res.is_correct is True
