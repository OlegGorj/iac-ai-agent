# LLM Factory Project

This project implements an LLM (Large Language Model) factory using LangChain packages. It provides a structured way to create and manage LLM instances with support for both local access and access through an authenticated gateway.

## Overview

The LLM Factory allows users to easily configure and instantiate language models, providing flexibility in how these models are accessed and utilized.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

1. **Configuration**: Set up your configuration in `src/config/settings.py`. This includes API keys and model parameters.

2. **Creating an LLM Instance**:
   ```python
   from src.factory.llm_factory import LLMFactory

   llm = LLMFactory(model='your_model_name', parameters={'param1': 'value1'})
   ```

3. **Accessing the Model**:
   - **Local Access**:
     ```python
     local_output = llm.local_access(input_data)
     ```

   - **Authenticated Gateway Access**:
     ```python
     gateway_output = llm.gateway_access(input_data)
     ```

## Testing

To run the tests, use:

```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.