import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Aula
from pypro.modulos.models import Modulo


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def response(client, aula):
    response = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return response


def test_titulo(response, aula: Aula):
    assert_contains(response, aula.titulo)
