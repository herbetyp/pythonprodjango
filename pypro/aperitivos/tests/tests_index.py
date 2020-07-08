import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp_indice(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code_indice(resp_indice):
    assert resp_indice.status_code == 200


@pytest.mark.parametrize(
    'titulo', ['Vídeo Aperitivo: Motivação', 'Instalação no Windows']
)
def test_titulo_video(resp_indice, titulo):
    assert_contains(resp_indice, titulo)


@pytest.mark.parametrize('slug', ['motivacao', 'instalacao-windows'])
def test_link_video(resp_indice, slug):
    video_link = reverse('aperitivos:video', args=[slug])
    assert_contains(resp_indice, f'href="{video_link}"')
