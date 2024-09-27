from flask import Flask, request, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Fonction pour générer une clé de cryptage (tu peux la stocker en base de données si besoin)
def generate_key():
    return Fernet.generate_key()

# Fonction pour chiffrer un message avec une clé
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message.decode()

# Fonction pour déchiffrer un message avec une clé
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message.encode())
    return decrypted_message.decode()

# Route pour chiffrer un message
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    message = data.get("message")
    key = data.get("key")
    if not message or not key:
        return jsonify({"error": "Message et clé sont requis."}), 400
    encrypted_message = encrypt_message(message, key)
    return jsonify({"encrypted_message": encrypted_message})

# Route pour déchiffrer un message
@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    encrypted_message = data.get("encrypted_message")
    key = data.get("key")
    if not encrypted_message or not key:
        return jsonify({"error": "Message chiffré et clé sont requis."}), 400
    try:
        decrypted_message = decrypt_message(encrypted_message, key)
        return jsonify({"decrypted_message": decrypted_message})
    except:
        return jsonify({"error": "Clé incorrecte ou message invalide."}), 400

# Route par défaut pour la page d'accueil
@app.route('/')
def home():
    return "Bienvenue à l'API de cryptage. Utilisez /encrypt pour chiffrer un message et /decrypt pour le déchiffrer."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
