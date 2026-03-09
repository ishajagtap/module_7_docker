import qrcode
import sys

def generate_qr_code(data, filename="qrcode.png"):
    """
    Generates a QR code from the given data and saves it as an image file.
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"Success! QR code successfully generated and saved to {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("=== QR Code Generator ===")
    data_to_encode = input("Enter the data or URL to encode: ")
    
    if not data_to_encode.strip():
        print("Data cannot be empty. Exiting.")
        sys.exit(1)
        
    output_filename = input("Enter the output filename (press enter for default 'qrcode.png'): ")
    
    if not output_filename.strip():
        output_filename = "qrcode.png"
    elif not output_filename.endswith(('.png', '.jpg', '.jpeg')):
        output_filename += ".png"
        
    generate_qr_code(data_to_encode, output_filename)
