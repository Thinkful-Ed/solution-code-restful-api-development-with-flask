# error-handling-api.py

from flask import Flask, jsonify

app = Flask(__name__)

# Define a custom error handler for 404 Not Found errors
@app.errorhandler(404)
def handle_404(error):
    # Create a dictionary with error details
    error_details = {
        "status": 404,
        "error": "Not Found",
        "message": f"Resource not found: {str(error)}"
    }
    # Return a JSON response with error details and status code
    return jsonify(error_details), 404

# Define a custom error handler for 500 Internal Server Error errors
@app.errorhandler(500)
def handle_500(error):
    # Create a dictionary with error details
    error_details = {
        "status": 500,
        "error": "Internal Server Error",
        "message": "An unexpected error occurred. Please try again later."
    }
    # Return a JSON response with error details and status code
    return jsonify(error_details), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)