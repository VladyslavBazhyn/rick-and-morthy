from django.contrib import admin
from django.urls import path

from rick_and_morthy.views import get_random_character, CharacterListView

app_name = "characters"

urlpatterns = [
    path("characters/random", get_random_character, name="character-random"),
    path("characters/", CharacterListView.as_view(), name="character-list")
]
