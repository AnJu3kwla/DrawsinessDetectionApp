import cv2

img = cv2.imread('test3.jpg')
roi = img[269: 795, 537: 1416]

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

#print(contours[0])

for cnt in contours:
    (x, y, w, h) = cv2.boundingRect(cnt)
    cv2.rectangle(roi, (x,y), (x + w , y+ h), (255, 0, 0), 2)

#cv2.drawContours(roi, contours, -1, (0, 255, 0), 3)
#cv2.drawContours(imgray, contours, -1, (255, 0, 0),3)
#cv2.drawContours(thresh, contours, -1, (0, 0, 255),3)

cv2.imshow('Image', roi)
cv2.imshow('Image Gray', imgray)
cv2.imshow("Image Treshold", thresh)

cv2.waitKey(0)
cv2.desttroyAllWindows()