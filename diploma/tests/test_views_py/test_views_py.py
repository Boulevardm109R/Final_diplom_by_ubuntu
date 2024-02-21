from django.test import TestCase
import pytest
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from backend.views import HomepageView, CustomAuthToken
import pytest
from django.urls import reverse
from django.test import Client
from backend.forms import CustomUserCreationForm

@pytest.fixture
def factory():
    return RequestFactory()

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def token(user):
    return Token.objects.create(user=user)

def test_homepage_view(factory):
    request = factory.get(reverse('homepage'))
    view = HomepageView.as_view()
    response = view(request)
    assert response.status_code == 200
    assert response.template_name == 'homepage.html'
    assert response.context_data['page_title'] == 'Главная'

def test_custom_auth_token_view(factory, user, token):
    request = factory.get(reverse('custom_auth_token'))
    request.user = user
    view = CustomAuthToken.as_view()
    response = view(request)
    assert response.status_code == 200
    assert 'token' in response.data
    assert 'email' in response.data
# Create your tests here.
@pytest.fixture
def client():
    return Client()

def test_signup_view(client):
    url = reverse('signup')
    response = client.get(url)
    assert response.status_code == 200

def test_signup_view_post(client):
    url = reverse('signup')
    data = {
        'username': 'testuser',
        'password1': 'testpassword',
        'password2': 'testpassword',
        'email': 'test@example.com',
        'type': 'distributor'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('homepage')

def test_login_view(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200

def test_login_view_post(client):
    url = reverse('login')
    data = {
        'username': 'testuser',
        'password': 'testpassword'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('homepage')