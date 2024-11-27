import cv2
import numpy as np

## Image file object
class ImageFile():

    ## Initialize and read the image from the given filepath
    def __init__(self,filepath) -> None:
        super().__init__()
        self.image = cv2.imread(filepath)
        return

    ## Resize the image
    def resize(self,width,height,method = "LINEAR") -> None:
        methods = ["NEAREST","LINEAR","CUBIC","LANCZOS4"]
        ## Raise exception if given invalid method type
        if method not in methods:
            raise Exception("Must use one of the following methods: 'NEAREST','LINEAR','CUBIC' or 'LANCZOS4'")
        if method == "LINEAR":
            _method = cv2.INTER_LINEAR   
        elif method == "NEAREST":
            _method = cv2.INTER_NEAREST
        elif method == 'CUBIC':
            _method = cv2.INTER_CUBIC
        else:
            _method = cv2.INTER_LANCZOS4

        ## Resize the image give width and height
        self.image = cv2.resize(self.image,(height,width),interpolation = _method)
        return

    ## Do bitwise AND operation with given image
    def Bitwise_AND(self,image) -> None:
        self.image = cv2.bitwise_and(self.image,image)
        return
    
    ## Do bitwise OR operation with given image
    def Bitwise_OR(self,image) -> None:
        self.image = cv2.bitwise_or(self.image,image)
        return
    
    ## Bitwise shift to right
    def Bitwise_shift_right(self,shift) -> None:
        self.image = self.image >> shift
        return

    ## Bitwise shift to left
    def Bitwise_shift_left(self,shift) -> None:
        self.image = self.image << shift
        return

    ## Return image
    def get(self) -> cv2.typing.MatLike:
        return self.image
    
    ## Return Image Width
    def getWidth(self) -> int:
        return self.image.shape[0]
    
    ## Return Image Height
    def getHeight(self) -> int:
        return self.image.shape[1]
    
    def show(self) -> None:
        cv2.imshow('Image',self.image)
        cv2.waitKey(0) 
        return
    
    def saveAs(self,filename) -> None:
        cv2.imwrite(filename,self.image)
        return
    
    def FourBitsImage(self) -> np.typing:
        image = np.zeros((self.getWidth(),self.getHeight(), 3),np.uint8)
        image[:,:,:] = 0xf0
        return image