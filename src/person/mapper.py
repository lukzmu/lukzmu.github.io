from typing import Any, Dict

from person.dto import Person, SocialMedia


class PersonMapper:
    @staticmethod
    def dict_to_dto(person: Dict[str, Any]) -> Person:
        return Person(
            name=person["name"],
            avatar=person["avatar"],
            title=person["title"],
            social_media=[
                SocialMedia(
                    icon=social["icon"],
                    link=social["link"],
                )
                for social in person.get("social", [])
            ],
        )
