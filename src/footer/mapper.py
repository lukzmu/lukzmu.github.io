from typing import Any, Dict

from footer.dto import FooterLink


class FooterLinkMapper:
    @staticmethod
    def dict_to_dto(footer_link: Dict[str, Any]) -> FooterLink:
        return FooterLink(
            icon=footer_link["icon"],
            link=footer_link["link"],
        )
