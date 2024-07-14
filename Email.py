import qrcode
import os

def generate_email_qr_code(email, subject, body, file_path='email_qrcode.png'):
    mailto = f"mailto:{email}?subject={subject}&body={body}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(mailto)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)
    print(f"Email QR code saved to {file_path}")

email = 'john.doe@example.com'
subject = 'Hello'
body = 'This is a test email.'
file_path = os.path.expanduser('~/Desktop/email_qrcode.png')
generate_email_qr_code(email, subject, body, file_path)