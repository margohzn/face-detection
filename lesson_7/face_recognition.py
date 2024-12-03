import cv2

haarcascade = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(haarcascade)

face_image = cv2.imread("face.jpg")
group_people = cv2.imread("group_people.jpg")

cv2.imshow("Face image", face_image)
cv2.imshow("Group image", group_people)

cv2.waitKey(0)
cv2.destroyAllWindows()