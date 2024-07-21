# Git Pull Automation script

This Flask application provides endpoints to automate the `git pull` operation for three different repositories. It listens for HTTP POST requests and performs a `git pull` operation in the respective local repository directory upon receiving a valid payload.

## Features

- Three endpoints to handle `git pull` operations for three different repositories (`repo1`, `repo2`, and `repo3`).
- Validates the incoming payload to ensure it contains the necessary information before executing the `git pull`.
- Returns the output of the `git pull` command as a JSON response.

## Endpoints

### `/repo1` (POST)
Pulls the latest changes from the remote repository to the local repository for `repo1`.

### `/repo2` (POST)
Pulls the latest changes from the remote repository to the local repository for `repo2`.

### `/repo3` (POST)
Pulls the latest changes from the remote repository to the local repository for `repo3`.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:

2. Navigate to the project directory:
    ```bash
    cd your-repository-directory
    ```
3. Install the required dependencies:
    ```bash
    pip install Flask
    ```


## Usage

1. Run the Flask application:
    ```bash
    python autogitpull-flask.py
    ```
2. The application will start and listen on port `999` by default.

## Discord notification

`autogitpull-flask2.py` features sending a message to discord via webhook. If you want to see the commit histories on Discord, feel free to use autogitpull-flask2.
You will need to `pip install requests datetime` in order to properly use it.
