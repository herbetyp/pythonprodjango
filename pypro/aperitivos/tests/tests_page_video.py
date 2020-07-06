import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp_motivacao(client):
    return client.get(reverse('aperitivos:video', args=['motivacao']))


@pytest.fixture
def resp_instalacao_windows(client):
    return client.get(reverse('aperitivos:video', args=['instalacao-windows']))


def test_status_code_motivacao(resp_motivacao):
    assert resp_motivacao.status_code == 200


def test_title_video_motivacao(resp_motivacao):
    assert_contains(resp_motivacao, '<h1>Vídeo Aperitivo: Motivação</h1>')


def test_content_video_motivacao(resp_motivacao):
    assert_contains(
        resp_motivacao, '<iframe src="https://player.vimeo.com/video/434538400"'
    )


def test_status_code_instalacao_windows(resp_instalacao_windows):
    assert resp_instalacao_windows.status_code == 200


def test_title_video_instalacao_windows(resp_instalacao_windows):
    assert_contains(resp_instalacao_windows, '<h1>Instalação no Windows</h1>')


def test_content_video_instalacao_windows(resp_instalacao_windows):
    assert_contains(
        resp_instalacao_windows,
        '<iframe src="https://player.vimeo.com/video/435485443"',
    )
