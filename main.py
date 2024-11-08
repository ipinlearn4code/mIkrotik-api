from flask import Flask, jsonify, request
from config.api_key import API_KEY
from core.services.ppp_secret_service import PPPSecretService

app = Flask(__name__)
ppp_secret_service = PPPSecretService()

# Endpoint untuk menambahkan PPP Secret
def require_api_key(f):
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key') or request.args.get('api_key')
        if api_key != API_KEY:
            # print(api_key)
            print(API_KEY)
            print("Is compared with")
            print(api_key)
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@app.route('/ppp-secret', methods=['POST'])
@require_api_key
def create_ppp_secret():
    data = request.json
    name = data.get('name')
    password = data.get('password')
    profile = data.get('profile')
    if not all([name, password, profile]):
        return jsonify({"error": "Name, password, and profile are required"}), 400
    
    ppp_secret_service.create(name=name, password=password, profile=profile)
    return jsonify({"message": f"PPP Secret '{name}' created successfully."}), 201

# Endpoint untuk membaca PPP Secret berdasarkan nama
@app.route('/ppp-secret/<name>', methods=['GET'])
@require_api_key
def get_ppp_secret(name):
    secret = ppp_secret_service.read(name=name)
    if secret:
        return jsonify(secret)
    return jsonify({"error": f"PPP Secret '{name}' not found"}), 404

# Endpoint untuk membaca semua PPP Secret
@app.route('/ppp-secret', methods=['GET'])
@require_api_key
def get_all_ppp_secrets():
    secrets = ppp_secret_service.read_all()
    return jsonify(secrets)

# Endpoint untuk memperbarui PPP Secret
@app.route('/ppp-secret/<name>', methods=['PUT'])
@require_api_key
def update_ppp_secret(name):
    data = request.json
    new_password = data.get('password')
    new_profile = data.get('profile')
    if ppp_secret_service.update(name=name, new_password=new_password, new_profile=new_profile):
        return jsonify({"message": f"PPP Secret '{name}' updated successfully."})
    return jsonify({"error": f"PPP Secret '{name}' not found"}), 404

# Endpoint untuk menonaktifkan PPP Secret
@app.route('/ppp-secret/<name>/disable', methods=['POST'])
@require_api_key
def disable_ppp_secret(name):
    if ppp_secret_service.disable(name=name):
        return jsonify({"message": f"PPP Secret '{name}' disabled successfully."})
    return jsonify({"error": f"PPP Secret '{name}' not found"}), 404

# Endpoint untuk mengaktifkan PPP Secret
@app.route('/ppp-secret/<name>/enable', methods=['POST'])
@require_api_key
def enable_ppp_secret(name):
    if ppp_secret_service.enable(name=name):
        return jsonify({"message": f"PPP Secret '{name}' enabled successfully."})
    return jsonify({"error": f"PPP Secret '{name}' not found"}), 404

# Endpoint untuk menghapus PPP Secret
@app.route('/ppp-secret/<name>', methods=['DELETE'])
@require_api_key
def delete_ppp_secret(name):
    if ppp_secret_service.delete(name=name):
        return jsonify({"message": f"PPP Secret '{name}' deleted successfully."})
    return jsonify({"error": f"PPP Secret '{name}' not found"}), 404

# Menjalankan API Flask
if __name__ == '__main__':
    app.run(debug=True, port=8888)
