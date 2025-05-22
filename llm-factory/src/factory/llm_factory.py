class LLMFactory:
    def __init__(self, model_name: str, model_params: dict):
        self.model_name = model_name
        self.model_params = model_params

    def access_model(self, use_gateway: bool = False):
        if use_gateway:
            from ..auth.gateway import AuthGateway
            gateway = AuthGateway()
            return gateway.access_model(self.model_name, self.model_params)
        else:
            return self._load_model_locally()

    def _load_model_locally(self):
        # Logic to load the model locally
        return f"Model {self.model_name} loaded with parameters {self.model_params}"