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
def resp(client_with_logged_in_user, aula):
    response = client_with_logged_in_user.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return response


@pytest.fixture
def resp_not_user(client, aula):
    response = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return response


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(
        resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{ modulo.titulo }</a></li>',
    )


def test_user_not_logged_redirect(resp_not_user):
    assert resp_not_user.status_code == 302
    assert resp_not_user.url.startswith(reverse('login'))
