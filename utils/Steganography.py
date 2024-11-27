def Steganography_encode(cover,hidden):
    hidden.Bitwise_shift_right(4)
    hidden.resize(cover.getWidth(),cover.getHeight())
    mask = hidden.FourBitsImage()
    cover.Bitwise_AND(mask)
    cover.Bitwise_OR(hidden.get())
    return cover

def Steganography_decode(cover):
    mask = cover.FourBitsImage()
    mask = mask >> 4
    cover.Bitwise_AND(mask)
    cover.Bitwise_shift_left(4)
    return cover