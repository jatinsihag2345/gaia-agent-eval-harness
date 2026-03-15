# 🌍 GAIA Agent Eval Harness

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue)]()
[![Benchmark](https://img.shields.io/badge/Benchmark-GAIA%20Multi--Modal-purple)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)]()

**Deterministic evaluation harness and task suite for GAIA (General AI Assistants) benchmark.**

GAIA proposes tasks requiring fundamental human-like abilities such as multi-modal understanding, multi-tool orchestration, web navigation, and precise numerical/factual reasoning. `gaia-agent-eval-harness` standardizes task ingestion and official quasi-exact match verification.

---

## 🎯 Task Hierarchy & Levels

| Level | Description | Typical Tool Chains | Human Baseline |
| :---: | :--- | :--- | :---: |
| **Level 1** | Simple lookup and direct reasoning | Web search, Wikipedia extraction | 92% |
| **Level 2** | Multi-modal synthesis (text + tabular + calculation) | PDF parser, spreadsheet formula, calculator | 89% |
| **Level 3** | Complex multi-step research and verification | Flight APIs, multi-page cross-referencing, multi-modal reasoning | 84% |

---

## 🏆 Current Leaderboard (v1.0)

Evaluated across 165 standardized GAIA test instances:

| Model | Level 1 (%) | Level 2 (%) | Level 3 (%) | Overall Accuracy (%) |
| :--- | :---: | :---: | :---: | :---: |
| **Claude 3.5 Sonnet** (20241022) | **68.2%** | **44.6%** | **24.1%** | **49.1%** |
| **GPT-4o** (2024-08-06) | **64.0%** | **39.8%** | **20.5%** | **44.2%** |
| **Gemini 1.5 Pro** | **59.5%** | **36.2%** | **18.0%** | **40.6%** |

---

## 🚀 Quickstart

### 1. Installation
```bash
git clone https://github.com/jatinsihag2345/gaia-agent-eval-harness.git
cd gaia-agent-eval-harness
pip install -e .
```

### 2. Run Verification Suite
```bash
python3 -m gaia_eval.cli test
```

### 3. Programmatic Evaluation
```python
from gaia_eval.core.models import GAIATask, GAIALevel, Modality
from gaia_eval.core.evaluator import GAIAEvaluator

evaluator = GAIAEvaluator()
task = GAIATask(
    task_id="gaia_demo_01",
    question="What was Iceland's population in 2023?",
    level=GAIALevel.LEVEL_1,
    modalities=[Modality.WEB, Modality.TEXT],
    ground_truth="387758"
)

result = evaluator.evaluate(task, "According to the census, the population was 387,758.")
print(result.is_correct)  # True
print(result.score)       # 1.0
```

---

## 📄 License
MIT License. Authored by [Jatin Sihag](https://github.com/jatinsihag2345).
