from dataclasses import dataclass


@dataclass(frozen=True)
class FooterLink:
    icon: str
    link: str
