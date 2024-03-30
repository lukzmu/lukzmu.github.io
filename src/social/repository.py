from typing import List

import yaml
from social.dto import SocialMedia
from social.mapper import SocialMediaMapper


class SocialMediaRepository:
    def __init__(self, data_path: str) -> None:
        self._data_path = data_path

    def get_social_media_list(self) -> List[SocialMedia]:
        with open(self._data_path) as file:
            data = yaml.safe_load(file)
            return [
                SocialMediaMapper.dict_to_dto(social_media=social_media)
                for social_media in data["items"]
            ]


social_media_repository = SocialMediaRepository(data_path="data/social.yml")
