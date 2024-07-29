from rest_framework import serializers

from rick_and_morthy.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            "id",
            "api_id",
            "name",
            "species",
            "status",
            "genre",
            "image"
        ]
