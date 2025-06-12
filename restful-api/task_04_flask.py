#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    """
    Root endpoint that returns a welcome message.

    Returns:
        str: Welcome message.
    """
    return "Welcome to the Flask API!"

# Data endpoint
@app.route("/data", methods=["GET"])
def data():
    """
    Endpoint that returns a list of all usernames.

    Returns:
        Response: JSON response with list of usernames.
    """
    return jsonify(list(users.keys()))

# Status endpoint
@app.route("/status", methods=["GET"])
def status():
    """
    Status endpoint to verify the server is running.

    Returns:
        str: "OK" string.
    """
    return "OK"

# Users username endpoint
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Get user data by username.

    Args:
        username (str): The username to look up.

    Returns:
        Response: JSON response with user data or error message.
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

# Add_user endpoint
@app.route("/add_user", methods=["POST"])
def create_user():
    """
    Add a new user from JSON payload.

    Expected JSON body:
        {
            "username": "alice",
            "name": "Alice",
            "age": 25,
            "city": "Paris"
        }

    Returns:
        Response: JSON response with confirmation message and user data,
        or error message if validation fails.
    """
    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run()
