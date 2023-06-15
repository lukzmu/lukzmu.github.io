from typing import List

import yaml
from footer.dto import FooterLink
from footer.mapper import FooterLinkMapper


class FooterLinkRepository:
    def __init__(self, data_path: str) -> None:
        self._data_path = data_path

    def get_footer_link_list(self) -> List[FooterLink]:
        with open(self._data_path) as file:
            data = yaml.safe_load(file)
            return [
                FooterLinkMapper.dict_to_dto(footer_link=footer_link)
                for footer_link in data["items"]
            ]


footer_repository = FooterLinkRepository(data_path="data/footer_links.yml")
