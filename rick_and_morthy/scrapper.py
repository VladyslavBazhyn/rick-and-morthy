import requests
from django.conf import settings

from rick_and_morthy.models import Character


def scrape_characters() -> list[Character]:
    next_url_to_scrape = settings.RICK_AND_MORTHY_API_CHARACTERS_URL

    characters = []
    while next_url_to_scrape is not None:
        characters_response = requests.get(
            next_url_to_scrape
        ).json()
        for character_dict in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character_dict.get("id"),
                    name=character_dict.get("name"),
                    status=character_dict.get("status"),
                    gender=character_dict.get("gender"),
                    species=character_dict.get("species"),
                    image=character_dict.get("image")
                )
            )
        next_url_to_scrape = characters_response.get("info").get("next")
    return characters


def save_characters(characters: list) -> None:
    for character in characters:
        character.save()


def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)
