#!/usr/bin/python3
"""Secure Flask API with Basic Auth and JWT."""
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

# Initialisation de l'application Flask
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "cle-secrete-ultra-securisee"

# Configuration des extensions
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Base d'utilisateurs en mémoire avec mot de passe haché et rôle
users = {
    "bob": {
        "username": "bob",
        "password": generate_password_hash("toto"),
        "role": "user"
    },
    "admin": {
        "username": "admin1",
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Vérifie les identifiants pour Basic Auth.

    Args:
        username (str): Nom d'utilisateur.
        password (str): Mot de passe en clair.

    Returns:
        bool: True si le mot de passe correspond, False sinon.
    """
    if username in users:
        return check_password_hash(users[username]["password"], password)
    return False


@app.route('/basic-protected')
@auth.login_required
def protected():
    """
    Route protégée par authentification basique.

    Returns:
        str: Message d'autorisation si identifiants valides.
    """
    return jsonify(message="Basic Auth: Access Granted")


@app.route("/login", methods=['POST'])
def login():
    """
    Authentifie un utilisateur et génère un token JWT.

    Returns:
        JSON: access_token si les identifiants sont valides.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Route protégée par JWT.

    Returns:
        str: Message d'accès autorisé si le token est valide.
    """
    return "JWT Auth: Access Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Gestion du token manquant ou invalide.

    Args:
        err (str): Message d'erreur.

    Returns:
        JSON: Message d'erreur avec code 401.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Gestion d'un token invalide.

    Args:
        err (str): Message d'erreur.

    Returns:
        JSON: Message d'erreur avec code 401.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Gestion d'un token expiré.

    Args:
        jwt_header (dict): En-tête JWT.
        jwt_payload (dict): Données JWT.

    Returns:
        JSON: Message d'erreur avec code 401.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """
    Gestion d'un token révoqué.

    Args:
        jwt_header (dict): En-tête JWT.
        jwt_payload (dict): Données JWT.

    Returns:
        JSON: Message d'erreur avec code 401.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    Gestion d'un token non frais.

    Args:
        jwt_header (dict): En-tête JWT.
        jwt_payload (dict): Données JWT.

    Returns:
        JSON: Message d'erreur avec code 401.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    # Lancement de l'application Flask en mode debug
    app.run(debug=True)
