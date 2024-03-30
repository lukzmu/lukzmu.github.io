from dataclasses import dataclass


@dataclass(frozen=True)
class SocialMedia:
    name: str
    icon: str
    url: str
