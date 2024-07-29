import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from rick_and_morthy.models import Character
from rick_and_morthy.serializers import CharacterSerializer


@api_view(["GET"])
def get_random_character(request: Request) -> Response:
    pks = Character.objects.values_list("pk", flat=True)
    try:
        random_pks = random.choice(pks)
    except IndexError:
        return Response(None)
    random_character = Character.objects.get(pk=random_pks)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data)
