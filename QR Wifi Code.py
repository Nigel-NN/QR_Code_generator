import qrcode
import os

def generate_wifi_qr_code(ssid, password, security, file_path='wifi_qrcode.png'):
    """
    Generates a WiFi QR code and saves it to a file.

    :param ssid: The SSID of the WiFi network.
    :param password: The password of the WiFi network.
    :param security: The security type (WPA, WEP, or nopass).
    :param file_path: The path where the QR code image will be saved.
    """
    # Create the WiFi configuration string
    wifi_config = f"WIFI:T:{security};S:{ssid};P:{password};;"

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add WiFi configuration to the QR code
    qr.add_data(wifi_config)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    img.save(file_path)
    print(f"WiFi QR code saved to {file_path}")

# Example usage: Generate a WiFi QR code for a network
ssid = 'Your_SSID'
password = 'Your_Password'
security = 'WPA'  # Security type can be 'WPA', 'WEP', or 'nopass'

# Get the path to the Desktop directory
desktop_path = os.path.expanduser('~/Desktop/wifi_qrcode.png')

# Generate and save the WiFi QR code to the Desktop directory
generate_wifi_qr_code(ssid, password, security, desktop_path)