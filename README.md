# Valve analytics Web-app

### Pre-requirements

**Use the following command in the root project directory**
```bash
chmod +x install.sh
./install.sh
```
* `install.sh` script is responsible for
    - Install poetry
    - Install project dependencies provided in `pyproject.toml`
    - Install pre-commit hooks, that will automatically apply linters, described in the
    `.pre-commit-config.yaml` file, when you'll try to commit your changes

Read more about `poetry` [here](https://python-poetry.org/docs/cli/) and about `pre-commit` [here](https://pre-commit.com/)

### How to run project

```bash
docker-compose up --build
```
Install docker [here](https://docs.docker.com/engine/install/)
P.S. post-installation step for linux users [here](https://docs.docker.com/engine/install/linux-postinstall/)
