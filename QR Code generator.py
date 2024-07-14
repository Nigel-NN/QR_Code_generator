import qrcode
from PIL import Image
import os

def generate_qr_code(data, file_path='qrcode.png', box_size=10, border=4):
    """
    Generates a QR code from the given data and saves it to a file.

    :param data: The data to encode in the QR code (e.g., URL).
    :param file_path: The path where the QR code image will be saved.
    :param box_size: Size of each box in the QR code grid.
    :param border: Size of the border (minimum is 4).
    """
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    img.save(file_path)
    print(f"QR code saved to {file_path}")


# Example usage: Generate a QR code for a URL
link = 'google.com'

# Get the path to the Documents directory
documents_path = os.path.expanduser('~/Documents/google_qrcode.png')

# Generate and save the QR code to the Documents directory
generate_qr_code(link, documents_path)