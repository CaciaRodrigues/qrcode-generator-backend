from flask import Flask, request, jsonify
from flask_cors import CORS  # Importando o CORS
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)
CORS(app)  # Ativando o CORS para o Flask

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get('text')
    if not data:
        return jsonify({"error": "Texto é obrigatório"}), 400

    img = qrcode.make(data)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return jsonify({"qr_code": img_base64})

if __name__ == '__main__':
    print("Iniciando o servidor Flask...")
    app.run(debug=True)
