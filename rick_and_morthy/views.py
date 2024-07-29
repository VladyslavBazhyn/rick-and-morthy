import random

from django.db.models import QuerySet
from rest_framework import status, generics
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


class CharacterListView(generics.ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self) -> QuerySet:

        queryset = Character.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset
