from utils.IO import ImageFile,FourBitsImage
import os

img1 = ImageFile(os.path.join(os.getcwd(),'Image-Encrypt-Decrypt-message\example-image.jpg'))
img2 = ImageFile(os.path.join(os.getcwd(),'Image-Encrypt-Decrypt-message\example-hidden-image.jpg'))

img2.show()
img2.Bitwise_shift_right(4)
img2.show()
mask = FourBitsImage(img1.getWidth(),img1.getHeight())
img1.show()
img1.Bitwise_AND(mask)
img1.show()
img2.resize(img1.getWidth(),img1.getHeight())
img1.Bitwise_OR(img2.get())
img1.show()
