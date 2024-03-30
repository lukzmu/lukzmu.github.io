from social.dto import SocialMedia
from social.mapper import SocialMediaMapper


class TestSocialMediaMapper:
    def test_social_media_mapper_parses_data_correctly(self, social_media_data):
        selected_social_media = social_media_data["items"][0]

        result = SocialMediaMapper.dict_to_dto(social_media=selected_social_media)

        assert type(result) is SocialMedia
        assert result.name == selected_social_media["name"]
        assert result.icon == selected_social_media["icon"]
        assert result.url == selected_social_media["url"]
