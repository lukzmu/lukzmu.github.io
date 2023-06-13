from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class SocialMedia:
    icon: str
    link: str


@dataclass(frozen=True)
class Person:
    name: str
    avatar: str
    title: str
    social_media: List[SocialMedia]
