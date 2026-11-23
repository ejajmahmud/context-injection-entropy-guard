"""Core Context Injection Entropy Guard implementation."""
import re
from typing import List, Tuple

class ScanVerdict:
    def __init__(self, is_suspicious: bool, detected_patterns: List[str], clean_text: str):
        self.is_suspicious = is_suspicious
        self.detected_patterns = detected_patterns
        self.clean_text = clean_text

class ContextInjectionGuard:
    INJECTION_PATTERNS = [
        ("override_instruction", re.compile(r"ignore\s+(all\s+)?(previous|prior)\s+instructions?", re.IGNORECASE)),
        ("system_prompt_leak", re.compile(r"(repeat|reveal|print)\s+(your\s+)?(system\s+prompt|initial\s+instructions)", re.IGNORECASE)),
        ("roleplay_jailbreak", re.compile(r"(you\s+are\s+now\s+in\s+developer\s+mode|dan\s+mode)", re.IGNORECASE)),
        ("tag_injection", re.compile(r"<\s*/?\s*(system|instruction|user_request)\s*>", re.IGNORECASE))
    ]

    @classmethod
    def scan_and_clean(cls, text: str) -> ScanVerdict:
        detected = []
        clean = text

        for name, pat in cls.INJECTION_PATTERNS:
            if pat.search(clean):
                detected.append(name)
                clean = pat.sub("[REDACTED_INJECTION_ATTEMPT]", clean)

        return ScanVerdict(len(detected) > 0, detected, clean)
