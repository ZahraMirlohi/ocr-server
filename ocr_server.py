from flask import Flask, request, jsonify
import base64
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    try:
        data = request.json
        image_base64 = data.get("imageBase64")
        if not image_base64:
            return jsonify({"error": "لطفاً تصویر Base64 ارسال کنید."}), 400

        # تبدیل Base64 به تصویر
        image_bytes = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_bytes))

        # OCR با زبان فارسی
        text = pytesseract.image_to_string(image, lang="fas")
        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
