from pypro.django_assertions import assert_contains
import pytest
from django.urls import reverse


@pytest.fixture
def response(client):
    resp = client.get(reverse('core:home'))
    return resp


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title>Python Pro</title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse("core:home")}">Python Pro</a>')
