from pypro.django_assertions import assert_contains
from django.test import Client
import pytest
from django.urls import reverse


@pytest.fixture
def response(client: Client):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title>Python Pro</title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse("home")}">Python Pro</a>')
