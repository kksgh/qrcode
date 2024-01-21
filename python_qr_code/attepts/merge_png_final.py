import PIL
from PIL import Image, ImageDraw, ImageFont
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask, SquareGradiantColorMask, RadialGradiantColorMask, HorizontalGradiantColorMask
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer, SquareModuleDrawer

def make_qrcode():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=6,
    border=0)
    qr.add_data('https://lk.profi-time.com/')

    #img = qr.make_image(fill_color="blue", back_color="white")

    #telegram = Image.open("backs/teleg.png")

    #telegram = telegram.convert("RGBA")

    qr_img2 = qr.make_image(image_factory=StyledPilImage,
                       module_drawer=RoundedModuleDrawer(), color_mask=HorizontalGradiantColorMask(left_color=(0, 136, 204), right_color=(54, 3, 150)))
    
    #return qr_img2
    qr_img2.save('fin.png', quality = 10)

def write_text():
    img = Image.open("fin.png")

    I1 = ImageDraw.Draw(img)

    myFont = ImageFont.truetype('backs/Ubuntu-Bold.ttf', 30)

    I1.text((50, 300), "@PROFI-TIME", fill=(0, 136, 204), font=myFont)

    img.save("finale_defi.png", quality = 10)
    
def combine():
    file1 = "backs/real_back.png"

    file2 = "fin.png"

    background = Image.open(file1)

    frontImage = Image.open(file2) 

    frontImage = frontImage.convert("RGBA") 
 
    background = background.convert("RGBA")

    width = (background.width - frontImage.width) // 2
  
    height = (background.height - frontImage.height) // 4
 
    background.paste(frontImage, (width, height)) 
 
    background.save("fin.png", quality = 10)

make_qrcode()

combine()

write_text()

#РАМКА
#width, height= img.size
#pad = 30
#base_img = Image.new("RGBA",(width+pad, height+pad), color='black')

#base_img.paste(img,(pad//2, pad//2))
#base_img.show()
