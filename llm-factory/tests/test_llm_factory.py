import unittest
from src.factory.llm_factory import LLMFactory

class TestLLMFactory(unittest.TestCase):

    def setUp(self):
        self.model_name = "test-model"
        self.model_params = {"param1": "value1", "param2": "value2"}
        self.llm_factory = LLMFactory(model=self.model_name, params=self.model_params)

    def test_model_initialization(self):
        self.assertEqual(self.llm_factory.model, self.model_name)
        self.assertEqual(self.llm_factory.params, self.model_params)

    def test_local_access(self):
        result = self.llm_factory.access_model_locally()
        self.assertIsNotNone(result)

    def test_authenticated_gateway_access(self):
        gateway_url = "https://example.com/api"
        result = self.llm_factory.access_model_through_gateway(gateway_url)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()