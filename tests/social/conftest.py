import pytest
from social.repository import SocialMediaRepository


@pytest.fixture
def social_media_repository():
    def _social_media_repository(data_path="dummy_path"):
        return SocialMediaRepository(data_path=data_path)

    return _social_media_repository


@pytest.fixture
def social_media_data():
    return {
        "items": [
            {
                "name": "GitLab",
                "icon": "gitlab",
                "url": "https://gitlab.com/lukasz.zmudzinski",
            },
            {
                "name": "LinkedIn",
                "icon": "linkedin",
                "url": "https://www.linkedin.com/in/lukzmu/",
            },
        ]
    }
