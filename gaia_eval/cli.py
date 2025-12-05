import sys
import argparse
from .tasks.sample_tasks import ALL_GAIA_TASKS
from .core.evaluator import GAIAEvaluator


def test_evaluator():
    evaluator = GAIAEvaluator()
    print("\nRunning GAIA Evaluation Verification Suite:")
    print("=" * 65)

    test_cases = [
        (ALL_GAIA_TASKS[0], "The total population is 387,758 people.", True),
        (ALL_GAIA_TASKS[1], "28.4%", True),
        (ALL_GAIA_TASKS[2], "SQ637, JL711, NH801", True),  # Unordered set match
        (ALL_GAIA_TASKS[0], "450000", False)
    ]

    all_passed = True
    for task, pred, expected_outcome in test_cases:
        res = evaluator.evaluate(task, pred)
        ok = (res.is_correct == expected_outcome)
        status = "PASSED" if ok else "FAILED"
        print(f" -> [{status}] Task: {task.task_id} | Correct: {res.is_correct} ({res.notes})")
        if not ok:
            all_passed = False

    print("=" * 65)
    if all_passed:
        print("GAIA Evaluator successfully verified!\n")
    else:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="GAIA Agent Eval Harness CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("test", help="Run GAIA evaluator test suite")

    args = parser.parse_args()
    if args.command == "test":
        test_evaluator()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
