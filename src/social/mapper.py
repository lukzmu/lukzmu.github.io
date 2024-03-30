from typing import Any, Dict

from social.dto import SocialMedia


class SocialMediaMapper:
    @staticmethod
    def dict_to_dto(social_media: Dict[str, Any]) -> SocialMedia:
        return SocialMedia(
            name=social_media["name"],
            icon=social_media["icon"],
            url=social_media["url"],
        )
