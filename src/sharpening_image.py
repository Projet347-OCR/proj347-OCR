import cv2
import numpy as np

img = cv2.imread('data/images/floue.jpg', 0)
print(img)
# img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
#cv2.imwrite('data/images/permis_de_conduire.jpg', img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#-------------------------------------------------------------

def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=4.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened

image = cv2.imread('data/images/flou.png')
sharpened_image = unsharp_mask(image)
cv2.imwrite('nett.png', sharpened_image)
#-----------------------------------------------------------------------------
image = cv2.imread('data/images/flou.png')
kernel = np.array([[-1,-1,-1],
                    [-1, 9,-1],
                    [-1,-1,-1]])
sharpened = cv2.filter2D(image, -1, kernel) # applying the sharpening kernel to the input image & displaying it.
cv2.imshow('Image Sharpening', sharpened)
cv2.imwrite('plus_nett.png', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-----------------------------------------------------------------------------
image1 = cv2.imread('data/images/flou.png')
image1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
se=cv2.getStructuringElement(cv2.MORPH_RECT , (8,8))
bg=cv2.morphologyEx(image1, cv2.MORPH_DILATE, se)
out_gray=cv2.divide(image1, bg, scale=255)
out_binary=cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU )[1]

cv2.imshow('binary', out_binary)
cv2.imwrite('binary.png',out_binary)

cv2.imshow('gray', out_gray)
cv2.imwrite('gray.png',out_gray)

print("fin - Meriam")