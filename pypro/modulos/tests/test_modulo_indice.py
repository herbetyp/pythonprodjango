import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.modulos.models import Aula
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def aulas(modulos):
    aulas = []
    for modulo in modulos:
        aulas.extend(baker.make(Aula, 3, modulo=modulo))
    return aulas


@pytest.fixture
def resp(client, modulos, aulas):
    response = client.get(reverse('modulos:indice'))
    return response


def test_indice_disponivel(resp):
    assert resp.status_code == 200


# def test_titulo(response, modulo: Modulo):
#     assert_contains(response, modulo.get_absolute_url())


# def test_descricao(response, modulo: Modulo):
#     assert_contains(response, modulo.descricao)


# def test_publico(response, modulo: Modulo):
#     assert_contains(response, modulo.publico)
