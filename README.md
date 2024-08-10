# Template Project

This is a template project for a Python application using Poetry for dependency management and pytest for testing.


## Getting Started

### Prerequisites

- Python 3.8 or higher
- Poetry

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/rodneyxr/python-poetry-template.git
    cd python-poetry-template
    rm -rf .git
    ```

2. Install dependencies:

    ```sh
    poetry install
    ```

### Running the Application

```sh
poetry run python app/cli.py
```

### Running Tests

```sh
poetry run pytest --cov
```

#### Project Files
- `app/cli.py`: Entry point for the command-line interface.
- `app/logger.py`: Logger configuration.
- `test/hello_test.py`: Example test file.

#### Configuration
- `.vscode/launch.json`: VS Code launch configuration.
- `.vscode/settings.json`: VS Code settings.
- `pyproject.toml`: Project configuration file for Poetry.
- `poetry.lock`: Lock file for Poetry dependencies.

### License
This project is licensed under the MIT License.


Feel free to customize this README file further based on your specific project requirements.