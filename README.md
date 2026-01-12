# randomqrsite

This python script chooses a website from 1000 most used websites list and writes the qr that goes to that random selected website to `.png` file.

I didn't want the images to be overwritten so I added a feature in `save_qr` function that prevents overwrites and gives the file an indexed name.
```python
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
```

*Output after executing qr.py*

<img width="902" height="271" alt="image" src="https://github.com/user-attachments/assets/f04d6b4c-3bd7-4f80-ae8b-4e5199758d03" />

---

*The generated qr code that redirects to `hamariweb.com`*

<img width="290" height="290" alt="qrcode" src="https://github.com/user-attachments/assets/c53b8d72-f133-4a1c-9ee7-e067c0794001" />
