from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de usuario (por ejemplo, almacenados en una base de datos)
users = {
    "user1": {"password": "password1"},
    "user2": {"password": "password2"}
}

# Ruta para la autenticación de usuarios
@app.route('/authenticate', methods=['POST'])
def authenticate_user():
    auth_data = request.get_json()
    username = auth_data.get('username')
    password = auth_data.get('password')

    if username in users and users[username]['password'] == password:
        return jsonify({'authenticated': True}), 200
    else:
        return jsonify({'authenticated': False}), 401

# Ruta para obtener información básica del servicio
@app.route('/info', methods=['GET'])
def get_service_info():
    return jsonify({'service': 'authentication', 'status': 'running'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)