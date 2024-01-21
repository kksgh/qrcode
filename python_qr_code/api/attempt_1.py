from flask import Flask, jsonify, request
import qrcode
from io import BytesIO
import base64
import requests


app = Flask(__name__)

# Endpoint to generate a QR code
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get('data')  # Get data from the request body
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an in-memory BytesIO object to store the QR code image
    img = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(img)
    img.seek(0)
    

    #with open('house.webp', 'rb') as image_file:
    base64_bytes = base64.b64encode(img.read())
    base64_string = base64_bytes.decode()


    # Return the QR code image as a response                         encoded_string = base64.b64encode(image_file.read())
    return jsonify(base64_string)



if __name__ == '__main__':
    app.run(debug=True)
    