from typing import Any, Dict

from person.dto import Person


class PersonMapper:
    @staticmethod
    def dict_to_dto(person: Dict[str, Any]) -> Person:
        return Person(
            name=person["name"],
            avatar=person["avatar"],
            title=person["title"],
        )
