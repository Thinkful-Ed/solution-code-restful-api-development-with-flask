# api-path-versioning.py

from flask import Flask, jsonify

app = Flask(__name__)

# First version of the API endpoint
@app.route('/v1/users', methods=['GET'])
def get_users_v1():
    users = ["Anna", "Ella", "Mike"]
    return jsonify({"version": "v1", "users": users})

# Second version of the API endpoint
@app.route('/v2/users', methods=['GET'])
def get_users_v2():
    users = [
        {"id": 1, "name": "Anna", "email": "anna@example.com"},
        {"id": 2, "name": "Ella", "email": "ella@example.com"},
        {"id": 3, "name": "Mike", "email": "mike@example.com"}
    ]
    return jsonify({"version": "v2", "users": users})

if __name__ == '__main__':
    app.run(debug=True, port=5001)