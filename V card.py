import qrcode
import os
def generate_vcard_qr_code(name, phone, email, file_path='vcard_qrcode.png'):
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(vcard)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)
    print(f"vCard QR code saved to {file_path}")

name = 'John Doe'
phone = '+1234567890'
email = 'john.doe@example.com'
file_path = os.path.expanduser('~/Desktop/vcard_qrcode.png')
generate_vcard_qr_code(name, phone, email, file_path)