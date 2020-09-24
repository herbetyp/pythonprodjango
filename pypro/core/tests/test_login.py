import pytest
from django.urls import reverse
from model_bakery import baker


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


@pytest.fixture
def user(db, django_user_model):
    user_model = baker.make(django_user_model)
    password = 'senha'
    user_model.set_password(password)
    user_model.save()
    user_model.senha = password

    return user_model


@pytest.fixture
def resp_post(client, user):
    return client.post(reverse('login'), {'username': user.email, 'password': user.senha})


def test_login_form_page(resp):
    assert resp.status_code == 200


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modulos:indice')
