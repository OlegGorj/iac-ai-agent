import unittest
from src.auth.gateway import AuthGateway

class TestAuthGateway(unittest.TestCase):

    def setUp(self):
        self.gateway = AuthGateway(api_key="test_api_key")

    def test_authenticate_success(self):
        result = self.gateway.authenticate("valid_username", "valid_password")
        self.assertTrue(result)

    def test_authenticate_failure(self):
        result = self.gateway.authenticate("invalid_username", "invalid_password")
        self.assertFalse(result)

    def test_access_model_local(self):
        model = self.gateway.access_model("local_model_id")
        self.assertIsNotNone(model)

    def test_access_model_authenticated(self):
        model = self.gateway.access_model("remote_model_id")
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()