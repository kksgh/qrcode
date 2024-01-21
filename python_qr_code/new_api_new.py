from flask import Flask, send_file
import qrcode

app = Flask(__name__)

@app.route('/generate_qr')
def generate_qr():
    # Get the text for the QR code (you can modify this as needed)
    data = "Hello, World!"

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image temporarily (you can save it to a file or serve directly)
    temp_filename = "temp_qr.png"
    img.save(temp_filename)

    # Send the image file as a response
    return send_file(temp_filename, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

if __name__ == '__main__':
    app.run(debug=True)


