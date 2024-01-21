import qrcode
from PIL import Image, ImageDraw, ImageFont
from qrcode.image.styles.colormasks import SolidFillColorMask, SquareGradiantColorMask, RadialGradiantColorMask, HorizontalGradiantColorMask

def generate_gradient(width, height, left_color, right_color):
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    for x in range(width):
        r = int(left_color[0] * (1 - x / (width - 1)) + right_color[0] * (x / (width - 1)))
        g = int(left_color[1] * (1 - x / (width - 1)) + right_color[1] * (x / (width - 1)))
        b = int(left_color[2] * (1 - x / (width - 1)) + right_color[2] * (x / (width - 1)))
        draw.line([(x, 0), (x, height)], fill=(r, g, b), width=1)
    return img

def generate_qr_with_text(data, text, gradient_width, gradient_height, left_color, right_color):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    #style = ColorMaskStyle(
    #    gradient=generate_gradient(gradient_width, gradient_height, left_color, right_color)
    #)

    qr_img = qr.make_image(fill='black', back_color='white')

    result_width = max(qr_img.size[0], gradient_width)
    result_height = qr_img.size[1] + gradient_height

    result = Image.new("RGB", (result_width, result_height), color="white")
    result.paste(qr_img, ((result_width - qr_img.size[0]) // 2, 0))

    draw = ImageDraw.Draw(result)
    text_font = ImageFont.load_default()
    text_width, text_height = draw.textsize(text, font=text_font)
    draw.text(((result_width - text_width) // 2, qr_img.size[1]), text, fill="black", font=text_font)

    return result

# Define colors
left_color = (0, 136, 204)
right_color = (54, 3, 150)

# Generate QR code with gradient and text
data_to_encode = "Your data here"
qr_with_gradient_and_text = generate_qr_with_text(data_to_encode, "@example", 300, 50, left_color, right_color)
qr_with_gradient_and_text.show()  # Display the QR code with gradient and text
