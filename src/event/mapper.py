from typing import Any, Dict

from event.dto import Event


class EventMapper:
    @staticmethod
    def dict_to_dto(event: Dict[str, Any]) -> Event:
        return Event(
            title=event["title"],
            subtitle=event.get("subtitle"),
            date=event["date"],
            icon=event.get("icon", ""),
            important=event.get("important", False),
        )
