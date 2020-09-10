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
def aulas(modulo):
    return baker.make(Aula, 3, modulo=modulo)


@pytest.fixture
def response(client, modulo, aulas):
    response = client.get(reverse('modulos:detalhe', kwargs={'slug': modulo.slug}))
    return response


def test_titulo(response, modulo: Modulo):
    assert_contains(response, modulo.get_absolute_url())


def test_descricao(response, modulo: Modulo):
    assert_contains(response, modulo.descricao)


def test_publico(response, modulo: Modulo):
    assert_contains(response, modulo.publico)


def test_aulas_titulos(response, aulas):
    for aula in aulas:
        assert_contains(response, aula.titulo)


def test_aulas_links(response, aulas):
    for aula in aulas:
        assert_contains(response, aula.get_absolute_url())
