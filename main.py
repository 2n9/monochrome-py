# picture to monochrome converter
import cv2
import os

def convert(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return thresh

def main():
    files = os.listdir('images')
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.JPG') or file.endswith('.PNG') or file.endswith('.JPEG'):
            img = cv2.imread('images/' + file)
            img = convert(img)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        cv2.imwrite('converted/' + file, img)

    print('Convert success')

if __name__ == '__main__':
    main()

