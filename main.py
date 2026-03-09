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
    import argparse
    import os
    
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument("--url", help="The data or URL to encode", type=str)
    parser.add_argument("--output", help="The output filename", type=str, default="qrcode.png")
    
    args = parser.parse_args()
    
    print("=== QR Code Generator ===")
    
    data_to_encode = args.url
    if not data_to_encode:
        # Fallback to interactive input if no argument was passed
        data_to_encode = input("Enter the data or URL to encode: ")
        
    if not data_to_encode or not data_to_encode.strip():
        print("Data cannot be empty. Exiting.")
        sys.exit(1)
        
    output_filename = args.output
    if not output_filename.endswith(('.png', '.jpg', '.jpeg')):
        output_filename += ".png"
        
    # Optional: Save to the qr_codes directory if it exists (for Docker)
    if os.path.exists("qrcodes"):
        output_filename = os.path.join("qrcodes", output_filename)
        
    generate_qr_code(data_to_encode, output_filename)
