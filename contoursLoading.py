import os
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

from glob import glob
try:
    # PIL
    import Image

except ImportError:
    # Pillow
    from PIL import Image

def process_image(img_path):
    print("Processing image: %s" % img_path)
    # Open the image
    img = Image.open(img_path)

    # Do your processing here
    print(img.info)

    # Not strictly necessary, but let's be explicit:
    # Close the image
    del img

images_dir = "F:/ANJANA/MY PROJECTS/Python/Project/data"

if __name__ == "__main__":
    # List all JPEG files in the directory
    #storing the whole directory in a list
    images_list = glob(os.path.join(images_dir, "*.jpg"))

for img_filename in images_list:
    img = cv2.imread(img_filename)
    roi = img[269: 795, 537: 1416]
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    imgray = cv2.GaussianBlur(imgray, (7,7), 0)

    ret, thresh = cv2.threshold(imgray, 4, 255, cv2.THRESH_BINARY_INV)

    contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    noOfContours = str(len(contours))
    if noOfContours == 0:
        cv2.puttext("Warning")
    else:
        print("number of contours = "+noOfContours)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(roi, (x,y), (x + w , y+ h), (255, 0, 0), 2)
         
    #cv2.imshow('image',img)  
    cv2.imshow('ROI',roi)  
    cv2.waitKey(0)           
    cv2.destroyAllWindows()
       