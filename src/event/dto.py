from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Event:
    title: str
    subtitle: Optional[str]
    date: str
    icon: str
    important: bool
