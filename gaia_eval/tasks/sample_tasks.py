from typing import List
from ..core.models import GAIATask, GAIALevel, Modality

TASK_GAIA_01 = GAIATask(
    task_id="gaia_lvl1_001",
    question="What was the total population of Iceland according to the official 2023 Statistics Iceland census?",
    level=GAIALevel.LEVEL_1,
    modalities=[Modality.WEB, Modality.TEXT],
    ground_truth="387758",
    annotator_metadata={"source": "statice.is"}
)

TASK_GAIA_02 = GAIATask(
    task_id="gaia_lvl2_014",
    question="Based on the quarterly financial table in 'q3_earnings.csv', calculate the EBITDA margin in percentage for the enterprise software division in Q3 2024.",
    level=GAIALevel.LEVEL_2,
    modalities=[Modality.TABLE, Modality.TEXT],
    ground_truth="28.4%",
    file_attachments=["q3_earnings.csv"],
    annotator_metadata={"calculation": "(EBITDA / Revenue) * 100"}
)

TASK_GAIA_03 = GAIATask(
    task_id="gaia_lvl3_029",
    question="List the three flight numbers departing from Tokyo Narita (NRT) to Singapore Changi (SIN) on October 15, 2024 operating non-stop Boeing 787 aircraft, separated by commas in alphabetical order.",
    level=GAIALevel.LEVEL_3,
    modalities=[Modality.WEB, Modality.TEXT, Modality.TABLE],
    ground_truth="JL711, NH801, SQ637",
    annotator_metadata={"steps_required": 7}
)

ALL_GAIA_TASKS: List[GAIATask] = [
    TASK_GAIA_01,
    TASK_GAIA_02,
    TASK_GAIA_03
]
