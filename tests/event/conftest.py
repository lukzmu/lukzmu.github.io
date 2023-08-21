import pytest
from event.repository import EventRepository


@pytest.fixture
def event_repository():
    def _event_repository(data_path="dummy_path"):
        return EventRepository(data_path=data_path)

    return _event_repository


@pytest.fixture
def event_data():
    return {
        "items": [
            {
                "title": "👰🏻‍♀️ Anna and Łukasz get married",
                "date": "May 2021",
            },
            {
                "title": "💍 Anna and Łukasz get engaged",
                "date": "September 2017",
            },
        ]
    }
