import requests
import base64

url = 'http://127.0.0.1:5000/generate_qr'
data = {'data': 'foff'}  # Your data to encode into the QR code

response = requests.post(url, json=data) 

if response.status_code == 200:
    # Save the received image
    base64_bytes = base64.b64encode() #(img.read())
    with open('qr_code1.png', 'wb') as f:
        f.write(response.content)
        print('QR code generated successfully and saved as qr_code1.png')
        f.write(base64.decodebytes(base64_bytes))
else:
    print('Failed to generate QR code')