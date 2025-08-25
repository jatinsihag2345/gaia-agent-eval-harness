from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Any, Dict


class GAIALevel(int, Enum):
    LEVEL_1 = 1  # Requires 1-3 tool steps, simple web/file lookup
    LEVEL_2 = 2  # Requires 4-8 steps, multi-modal synthesis (text + tabular + calculation)
    LEVEL_3 = 3  # Requires 9+ steps, complex multi-tool research and verification


class Modality(str, Enum):
    TEXT = "text"
    TABLE = "table"
    IMAGE = "image"
    PDF = "pdf"
    WEB = "web"


@dataclass
class GAIATask:
    task_id: str
    question: str
    level: GAIALevel
    modalities: List[Modality]
    ground_truth: str
    file_attachments: List[str] = field(default_factory=list)
    annotator_metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class GAIAEvaluationResult:
    task_id: str
    level: GAIALevel
    predicted_answer: str
    ground_truth: str
    is_correct: bool
    score: float
    notes: Optional[str] = None
