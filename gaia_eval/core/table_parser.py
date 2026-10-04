import csv
from typing import List, Dict, Any, Optional


class TableAttachmentParser:
    """
    Parses CSV and TSV tabular data attachments in GAIA multimodal tasks
    to support formula verification and column statistical checks.
    """

    @staticmethod
    def parse_csv(file_content: str, delimiter: str = ",") -> List[Dict[str, str]]:
        lines = file_content.strip().splitlines()
        if not lines:
            return []
        reader = csv.DictReader(lines, delimiter=delimiter)
        return [row for row in reader]

    @staticmethod
    def calculate_column_sum(rows: List[Dict[str, str]], column_name: str) -> Optional[float]:
        total = 0.0
        for r in rows:
            val = r.get(column_name, "").replace(",", "").replace("$", "").replace("%", "").strip()
            try:
                total += float(val)
            except ValueError:
                continue
        return total
