import pytest
from django.urls import reverse

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def video(db):
    vd = Video(slug='motivacao', titulo='Vídeo Aperitivo: Motivação', vimeo_id='434538400')
    vd.save()
    return vd


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=[video.slug]))


@pytest.fixture
def resp_video_nao_econtrado(client, video):
    return client.get(reverse('aperitivos:video', args=[video.slug + 'slug_nao_existe']))


def test_status_code(resp, video):
    assert resp.status_code == 200


def test_status_code_video_nao_encontrado(resp_video_nao_econtrado):
    assert resp_video_nao_econtrado.status_code == 404


def test_title_video(resp, video):
    assert_contains(resp, f'<h1>{video.titulo}</h1>')


def test_content_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')
