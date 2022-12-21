# Valve analytics Web-app

### Pre-requirements

0. Manage dependencies via poetry
* Install `poetry`

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
* Install dependencies (run in directory with **pyproject.toml**)

    ```bash
    poetry install
    ```
    Read more about `poetry` [here](https://python-poetry.org/docs/cli/)


1. Codestyle checks with `pre-commit`


* Use the following command on in the root project directory

    ```bash
    pre-commit install
    ```

    It will install pre-commit hooks, that will automatically apply linters, described in the *.pre-commit-config.yaml* file, when you'll try to commit your changes

    Read more about `pre-commit` [here](https://pre-commit.com/)
