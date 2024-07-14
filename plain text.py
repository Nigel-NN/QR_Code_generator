import qrcode
import os

def generate_text_qr_code(text, file_path='text_qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)
    print(f"Text QR code saved to {file_path}")

text = 'Hello, this is a QR code for plain text.'
file_path = os.path.expanduser('~/Desktop/text_qrcode.png')
generate_text_qr_code(text, file_path)