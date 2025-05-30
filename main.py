
from llm_factory_v1 import LLMFactory
from src.config.settings import Settings

settings = Settings()
factory = LLMFactory(settings)

# Create an LLM instance
try:
    llm = factory.create_llm(
        model_name=settings.default_model,
        params={"temperature": 0.5, "max_tokens": 150}
    )

    # Use the LLM
    if llm:
        response = llm("Tell me a joke.")
        print(response)
    else:
        print("Failed to create LLM.")

except ValueError as e:
    print(f"Error: {e}")
