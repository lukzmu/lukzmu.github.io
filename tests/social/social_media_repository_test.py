import json


class TestSocialMediaRepository:
    def test_social_media_repository_constructor(self, social_media_repository):
        data_path = "data/social.yml"
        repository = social_media_repository(data_path=data_path)

        assert repository._data_path == data_path

    def test_social_media_list_returns_correct_social_media_count(
        self, social_media_repository, social_media_data, mocker
    ):
        mocked_data = mocker.mock_open(read_data=json.dumps(social_media_data))
        mocker.patch("builtins.open", mocked_data)

        result = social_media_repository().get_social_media_list()

        assert len(result) == 2
