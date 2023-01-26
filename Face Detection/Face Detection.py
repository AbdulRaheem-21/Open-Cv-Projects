import cv2

faceCascade = cv2.CascadeClassifier(r"C:\Users\Abdul Raheem A\PycharmProjects\OpenCv Project\venv\Lib\site-packages\cv2\haarcascade_frontalface_default.xml")
img = cv2.imread(r"C:\Users\Abdul Raheem A\Downloads\github\Open CV\Face Detection\sample image before face detection.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 314), 2)
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
