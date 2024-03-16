from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de la base de datos de usuarios con sus credenciales
users = {
    "user1": {"password": "password1"},
    "user2": {"password": "password2"},
    # Agrega más usuarios si es necesario
}

# Ruta de autenticación del Ambassador
@app.route("/authenticate", methods=["POST"])
def authenticate():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not (username and password):
        return jsonify({"error": "Se requieren el nombre de usuario y la contraseña"}), 400

    if username in users and users[username]["password"] == password:
        return jsonify({"authenticated": True}), 200
    else:
        return jsonify({"authenticated": False}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)