import segno

def create_qrcode():
    qrcode = segno.make('https://lk.profi-time.com/')
    qrcode.save('fucking_segno.png', border=10, scale=10, light = None) 
    
create_qrcode()