# How to SETUP

* Install poetry `curl -sSL https://install.python-poetry.org | python -`
* Install poetry dependencies for project `poetry install`

# To run Project

* If you want preview data for testing run `start.ps1`
* If you dont, just apply migrations and migrate with `poetry run` and the respective command. After that `runserver`
* Create a superuser user dont forgetting `poetry run`
* If you ran the project with `start.ps1` you can also clear all data with `exit.ps1`
