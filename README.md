Generated using AI

# Python Code Interpreter Agent

A smart Python code execution agent built with LangChain that can write and execute Python code to answer questions. The agent uses GPT-4 Turbo to interpret questions and generate appropriate Python code responses.

## Features

- Automatically writes and executes Python code to answer questions
- Uses Python REPL for code execution
- Built-in error handling and debugging capabilities
- Powered by GPT-4 Turbo via OpenAI API
- Uses LangChain's React Agent framework for structured responses

## Prerequisites

- Python 3.x
- OpenAI API key (set in environment variables)
- Required packages (specified in Pipfile):
  - python-dotenv
  - langchain
  - langchain-openai
  - langchain-experimental

## Installation

1. Clone the repository
2. Install dependencies using Pipenv:
```bash
pipenv install
```
3. Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the main script:

```bash
python main.py
```

The agent can:
- Execute Python code to answer questions
- Debug and retry failed code attempts
- Generate code-based solutions
- Handle various Python programming tasks

Example usage (as shown in main.py):
```python
agent_executor.invoke(input={
    "input": "generate and save 3 QR codes that point to www.google.com"
})
```

## Project Structure

- `main.py` - Main script containing the code interpreter agent setup
- `Pipfile` & `Pipfile.lock` - Python dependency management files
- `.env` - Environment variables (not included in repo)

## How It Works

1. The agent is initialized with specific instructions about its role and capabilities
2. It uses LangChain's React Agent template as the base prompt
3. The Python REPL tool is provided for code execution
4. GPT-4 Turbo processes the input and generates appropriate Python code
5. The code is executed in a controlled REPL environment
6. Results are returned based on the code output

## Safety Features

- Only executes code within the Python REPL
- Returns "I don't know" for questions it cannot answer with code
- Always verifies answers by running code, even for simple calculations
- Includes error handling and debugging capabilities

## License

[Add your license information here]

## Contributing

[Add contribution guidelines if applicable]
