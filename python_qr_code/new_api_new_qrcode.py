from PIL import Image, ImageDraw, ImageFont
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask, SquareGradiantColorMask, RadialGradiantColorMask, HorizontalGradiantColorMask
from qrcode.image.styles.moduledrawers.pil import SquareModuleDrawer, RoundedModuleDrawer

def make_qrcode():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=6,
    border=0)
    qr.add_data('https://lk.profi-time.com/')

    #img = qr.make_image(fill_color="blue", back_color="white")

    #telegram = Image.open("backs/teleg.png")

    #telegram = telegram.convert("RGBA")

    qr_img = qr.make_image(image_factory=StyledPilImage,
                       module_drawer=SquareModuleDrawer(), 
                       #color_mask = SolidFillColorMask(back_color=(255, 255, 255), front_color=(34, 158, 217)))
                       color_mask=HorizontalGradiantColorMask(left_color=(34, 158, 217), right_color=(54, 3, 150)))
    
    return qr_img
    #qr_img.save('new_api_new_qrcode_1.png')
    
def combine():
    file1 = "backs/real_back.png"

    file2 = "new_api_new_qrcode_1.png"

    background = Image.open(file1)

    frontImage = Image.open(file2) 

    #frontImage = frontImage.convert("RGBA") 
 
    #background = background.convert("RGBA")

    width = (background.width - frontImage.width) // 2
  
    height = (background.height - frontImage.height) // 4
 
    background.paste(frontImage, (width, height)) 
 
    background.save("new_api_new_qrcode_1.png", quality = 20)
    #return background
    
def write_text():
    img = Image.open("new_api_new_qrcode_1.png")

    I1 = ImageDraw.Draw(img)

    myFont = ImageFont.truetype('backs/Ubuntu-Bold.ttf', 30)

    I1.text((50, 300), "@PROFI-TIME", fill=(0, 136, 204), font=myFont)

    img.save("new_api_new_qrcode_fin.png", quality = 20)

make_qrcode()

combine()

write_text()



