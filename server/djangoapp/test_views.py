from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
from ..views import logout_request

# test_views.py


class TestLogoutRequest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_logout_request(self):
        request = self.factory.get(reverse('logout'))
        request.user = AnonymousUser()

        response = logout_request(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertFalse(request.user.is_authenticated)
        self.assertFalse(request.session.items())