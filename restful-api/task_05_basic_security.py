#!/usr/bin/python3
"""Flask API server with authentication and authorization capabilities.
Implements both Basic Auth and JWT token-based authentication.
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

# Initialize the Flask application and authentication handlers
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key_ultra_secure'  # Secret key for signing JWTs
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users database with hashed passwords and roles
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
    Verify username and password for Basic Auth.

    Args:
        username (str): The provided username.
        password (str): The plain text password.

    Returns:
        dict or None: The user object if valid credentials, else None.
    """
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Endpoint protected by Basic Authentication.

    Returns:
        str: A message confirming access to the protected resource.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint that returns a JWT token if credentials are valid.

    Returns:
        JSON: A JWT access token or an error message with HTTP 401.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=
                                           {username : 'username',
                                            'role' : user['role']})

        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Endpoint protected by JWT Authentication.

    Returns:
        str: A message confirming access to the protected resource.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Endpoint accessible only to users with the 'admin' role.

    Returns:
        str: Success message if the user is an admin.
        JSON: Error message if the user lacks admin privileges.
    """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle requests with missing JWT tokens.

    Args:
        err (str): Error message.

    Returns:
        JSON: Error response with HTTP 401.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle requests with invalid JWT tokens.

    Args:
        err (str): Error message.

    Returns:
        JSON: Error response with HTTP 401.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle requests with expired JWT tokens.

    Args:
        err (str): Error message.

    Returns:
        JSON: Error response with HTTP 401.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle requests with revoked JWT tokens.

    Args:
        err (str): Error message.

    Returns:
        JSON: Error response with HTTP 401.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle requests that require a fresh JWT token.

    Args:
        err (str): Error message.

    Returns:
        JSON: Error response with HTTP 401.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
