import qrcode
import os
def generate_phone_qr_code(phone, file_path='phone_qrcode.png'):
    tel = f"tel:{phone}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(tel)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)
    print(f"Phone QR code saved to {file_path}")

phone = '+1234567890'
file_path = os.path.expanduser('~/Desktop/phone_qrcode.png')
generate_phone_qr_code(phone, file_path)