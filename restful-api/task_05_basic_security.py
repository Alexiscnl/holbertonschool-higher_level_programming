#!/usr/bin/python3
"""Secure Flask API with Basic Auth and JWT."""

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

# Initialize the Flask application
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "cle-secrete-ultra-securisee"

# Configure authentication extensions
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory user database with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify credentials for Basic Auth.

    Args:
        username (str): The username provided by the client.
        password (str): The plain text password to verify.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    if username in users:
        return check_password_hash(users[username]["password"], password)
    return False


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def protected():
    """
    Endpoint protected by Basic Authentication.

    Returns:
        JSON: Authorization message if credentials are valid.
    """
    return jsonify(message="Basic Auth: Access Granted")


@app.route("/login", methods=['POST'])
def login():
    """
    Authenticate user and return a JWT token.

    Returns:
        JSON: access_token if credentials are valid.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid credentials"}), 401

    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(users[username]["password"], password):
        # Include user role and username in the token identity
        identity = {
            "username": username,
            "role": users[username]["role"]
        }
        access_token = create_access_token(identity=identity)
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Endpoint protected by JWT Authentication.

    Returns:
        str: Authorization message if token is valid.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Endpoint restricted to users with admin role.

    Returns:
        str: Success message if user is admin, error if not.
    """
    current_user = get_jwt_identity()

    # Check if current_user is a dict (new format) or string (old format)
    if isinstance(current_user, dict):
        user_role = current_user.get('role')
    else:
        # Fallback for string identity - look up user in database
        user_role = users.get(current_user, {}).get('role')

    if user_role != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid JWT token.

    Args:
        err (str): Error message.

    Returns:
        JSON: Error message with 401 status code.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid JWT token.

    Args:
        err (str): Error message.

    Returns:
        JSON: Error message with 401 status code.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Handle expired JWT token.

    Args:
        jwt_header (dict): JWT header data.
        jwt_payload (dict): JWT payload data.

    Returns:
        JSON: Error message with 401 status code.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """
    Handle revoked JWT token.

    Args:
        jwt_header (dict): JWT header data.
        jwt_payload (dict): JWT payload data.

    Returns:
        JSON: Error message with 401 status code.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    Handle requests that require a fresh JWT token.

    Args:
        jwt_header (dict): JWT header data.
        jwt_payload (dict): JWT payload data.

    Returns:
        JSON: Error message with 401 status code.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    # Start the Flask development server in debug mode
    app.run(debug=True)
