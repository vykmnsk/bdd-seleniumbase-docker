# BDD UI tests

## Setup

Download and run _Python 3.x (64 bit)_ executable installer from [python.org](https://www.python.org/downloads/release/python-386/)

Verify python/pip are installed:

    python --version
    pip --version

 Create a virtual environment and install python libs (Windows CMD)

    python -m venv .venv
    .venv\Scripts\activate.bat
	pip install --upgrade pip
	pip install -r reqs.txt
    seleniumbase install chromedriver latest

## Run tests

### on Local machine

#### All tests

    > pytest
    if there are errors check ./latest_logs/ for run info, page source, screenshots

#### One Feature in Firefox

    > pytest -k Stays --browser=firefox

### in Local Docker container

    > docker build . -t pytest-bdd-seleniumbase
    > docker run pytest-bdd-seleniumbase

### on Github CI

    commit a change to "main" branch and navigate to this Github repo "Actions" tab