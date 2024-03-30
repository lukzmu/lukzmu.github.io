import os

from animal.repository import animal_repository
from event.repository import event_repository
from person.repository import person_repository
from social.repository import social_media_repository

# --- Site Data ---
SITEURL = os.getenv("SITEURL", default="https://zmudzinski.me")
AUTHOR = "Lukasz Zmudzinski"
SITENAME = "Anna and Łukasz"
TIMEZONE = "Europe/Warsaw"
DEFAULT_LANG = "en"

# --- Pelican Paths and Settings ---
PATH = "content"
THEME = "themes/core"
THEME_STATIC_DIR = "theme"
DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

# --- Feed Generation ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Site Data ---
SITE_DATA = {
    "people": person_repository.get_people_list(),
    "animals": animal_repository.get_animals_list(),
    "events": event_repository.get_event_list(),
    "social_media": social_media_repository.get_social_media_list(),
}
