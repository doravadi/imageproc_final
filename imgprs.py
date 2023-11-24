import cv2

def colorProfiles(n):
    if n == 0:
        name = "Pepsi"
        hsv_lower = (95, 100, 100)
        hsv_upper = (115, 255, 255)
        return (name, hsv_lower, hsv_upper)
    elif n == 1:
        name = "Coke"
        hsv_lower = (0, 100, 100)
        hsv_upper = (10, 255, 255)
        return (name, hsv_lower, hsv_upper)
    elif n == 2:
        name = "Fanta"
        hsv_lower = (10, 100, 100)
        hsv_upper = (30, 255, 255)
        return (name, hsv_lower, hsv_upper)
    elif n == 3:
        name = "Sprite"
        hsv_lower = (60, 100, 100)
        hsv_upper = (80, 255, 255)
        return (name, hsv_lower, hsv_upper)

def label_contour(img, contour, label):
    rect = cv2.boundingRect(contour)
    x, y, w, h = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.putText(img, label, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

frame = cv2.imread("fanta.jpg")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

threshold_area = 500  # Set an appropriate threshold area value based on your image characteristics

for i in range(4):  # Adjust the range based on the number of drinks
    name, hsv_lower, hsv_upper = colorProfiles(i)

    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
    conts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in conts:
        area = cv2.contourArea(contour)

        # Check if the contour has a large area and is within the specified HSV range
        if area > threshold_area and hsv_lower[0] <= hsv[contour[0][0][1], contour[0][0][0], 0] <= hsv_upper[0]:
            label_contour(frame, contour, name)

cv2.imshow("Image", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
