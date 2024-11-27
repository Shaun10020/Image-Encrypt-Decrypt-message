# Image-Steganography
This project is to encrypt and decrypt hidden image in another image.

Image Steganography hide image using least significant bits of another image. Humans are not sensitive to slight color change and Image Steganography is using this to encode the most significant bits of hidden image and replace the least significant bits of the cover image.

## Usage:
Steganography Encode
```
python main.py encode example-image.jpg Cover.png -hidden=example-hidden-image.jpg
```

Steganography Decode
```
python main.py decode Cover.png Hidden.png
```