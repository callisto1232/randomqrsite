import json
import os
import random
import qrcode

def get_random_domain(data):
    domains = [item['domain'] for item in data]
    return random.choice(domains)

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def save_qr(img):
    base_filename = "qrcode"
    extension = ".png"
    filename = f"{base_filename}{extension}"
    if os.path.exists(filename):
        number = 1
        while os.path.exists(f"{base_filename}{number}{extension}"):
            number += 1
        filename = f"{base_filename}{number}{extension}"
    img.save(filename)
    return filename

if __name__ == "__main__":
    with open('ranked_domains.json', 'r') as f:
        data = json.load(f)
    random_domain = get_random_domain(data)
    qr_img = generate_qr_code(random_domain)
    saved_filename = save_qr(qr_img)
    print(f"QR code generated and saved as {saved_filename}")

