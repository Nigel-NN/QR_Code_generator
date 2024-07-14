import qrcode
import os

def generate_geo_qr_code(latitude, longitude, file_path='geo_qrcode.png'):
    geo = f"geo:{latitude},{longitude}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(geo)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)
    print(f"Geo QR code saved to {file_path}")

latitude = '37.7749'
longitude = '-122.4194'
file_path = os.path.expanduser('~/Desktop/geo_qrcode.png')
generate_geo_qr_code(latitude, longitude, file_path)