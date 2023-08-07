from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    title: str
    date: str
    important: bool
