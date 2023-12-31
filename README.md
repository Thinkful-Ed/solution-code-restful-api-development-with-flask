# Solution Code RESTful API Development With Flask

## Objective

This repository contains a collection of Flask-based APIs demonstrating various functionalities:

- **Sentiment Analysis**: Analyzes the sentiment of textual content.
- **API Path Versioning**: Demonstrates how to version your API routes.
- **Custom Error Handling**: Implements custom error handlers for a Flask application.

## Installation

1. Clone this repository.
2. Navigate to the project directory:

   ```bash
   cd solution-code-restful-api-development-with-flask
   ```
3. Set up a virtual environment (recommended). Depending on your OS, use one of the following:
   - macOS and Linux:
     ```bash
     python -m venv solution-code-restful-api-development-with-flask-venv;
     source solution-code-restful-api-development-with-flask-venv/bin/activate;
     ```
   - Windows:
     ```bash
     python -m venv solution-code-restful-api-development-with-flask-venv
     .\solution-code-restful-api-development-with-flask-venv\Scripts\activate
     ```
4. Install the required packages (Flask should be in the `requirements.txt`):
   ```shell
   pip install -r requirements.txt
   ```
5. Run the desired API. Replace `file_name.py` with the specific API file you want to run:
   * By default, the API will start on `http://127.0.0.1:5001`
   ```bash
   # To Run: error-handling-api.py
   python error-handling-api.py

    # To Run: api-path-versioning.py
    python api-path-versioning.py

   # To Run: error-handling-api.py
   python error-handling-api.py
   ```

## API Descriptions

1. Sentiment Analysis API (`sentiment-analysis-api.py`):
   - Retrieve all data: `GET /data`
   - Add new data & analyze sentiment: `POST /data`
   - Update specific data content: `PUT /data/<id>`
   - Delete specific data: `DELETE /data/<id>`
2. API Path Versioning (`api-path-versioning.py`):
   - Get users for version 1: `GET /v1/users`
   - Get users for version 2 (with added details): `GET /v2/users`
3. Custom Error Handling API (`error-handling-api.py`):
   - If a route is not found or there's an internal server error, custom error handlers provide detailed error information.

## Notes

Each API file is designed to run independently. Make sure only one file is running at a time on the same port to avoid conflicts.