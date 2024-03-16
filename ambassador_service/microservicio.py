from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

AMBASSADOR_URL = "http://34.205.147.106:5000/authenticate"

# Ejemplo de solicitud de autenticación al Ambassador
def authenticate_user(username, password):
    data = {"username": username, "password": password}
    response = requests.post(AMBASSADOR_URL, json=data)
    return response.json()

# Ruta de ejemplo en un microservicio que necesita autenticación
@app.route("/protected", methods=["GET"])
def protected_resource():
    auth_data = request.headers.get("Authorization")
    if not auth_data:
        return jsonify({"error": "No se proporcionaron credenciales"}), 401

    # Simulación de validación de token de autenticación
    token = auth_data.split(" ")[1]
    
    # Aquí iría la lógica para enviar la solicitud de autenticación al Ambassador
    auth_response = authenticate_user("user1", "password1")
    
    if auth_response.get("authenticated"):
        return jsonify({"message": "Recurso protegido accedido"}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6379