import cv2
import numpy as np
#Read the image
image = cv2.imread("image.png")
if image is None:
    print("Error: Could not read the image.")
    exit()
#Resize the image
image=cv2.resize(image,(800,600))
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5),0)
#Apply Canny edge detection
edges = cv2.Canny(blur, 50, 150)
height, width = edges.shape
mask = np.zeros_like(edges)
points = np.array([[(0, height), (width // 2 - 50, height // 2), (width // 2 + 50, height // 2), (width, height)]], dtype=np.int32)
cv2.fillPoly(mask, points, 255)
road_edges = cv2.bitwise_and(edges, mask)
lines = cv2.HoughLinesP(road_edges, 1, np.pi / 180, 30, minLineLength=30, maxLineGap=100)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line.flatten()
        cv2.line(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 45), 4)
#display the image
cv2.imshow("Lane Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

