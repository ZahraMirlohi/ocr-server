from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import base64, io

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    try:
        data = request.json
        if not data or "imageBase64" not in data:
            return jsonify({"error": "imageBase64 is required"}), 400

        image_data = base64.b64decode(data['imageBase64'])
        image = Image.open(io.BytesIO(image_data))
        text = pytesseract.image_to_string(image, lang='fas')

        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "✅ OCR Server is running with Persian (fas) support!"
