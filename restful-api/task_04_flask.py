#!/usr/bin/python3
"""
A simple Flask API application demonstrating basic CRUD operations.

This module sets up a Flask web server with endpoints to:
- Serve a welcome message
- Provide status checks
- List, retrieve, create, update, and delete users in memory

Environment:
- Python 3
- Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }
}


@app.route("/")
def home():
    """
    Root endpoint.

    Returns:
        str: Welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Health check endpoint.

    Returns:
        str: "OK" if server is running.
    """
    return "OK"


@app.route("/data")
def list_users():
    """
    Retrieve all usernames.

    Returns:
        Response: JSON list of usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Retrieve details for a specific user.

    Args:
        username (str): The username identifier from the URL.

    Returns:
        Response: JSON user details or error message with status code.
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def create_user():
    """
    Create a new user from JSON payload.

    Expected JSON fields:
        - username (str): Unique user key
        - name (str): Full name of the user
        - age (int): Age of the user
        - city (str): City of residence

    Returns:
        Response: Success message with new user data or error message.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request must be JSON"}), 400

    for field in ["username", "name", "age", "city"]:
        if field not in data:
            return jsonify({"error": f"{field.capitalize()} is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    """
    Entry point for running the Flask development server.
    """
    app.run(debug=True)
