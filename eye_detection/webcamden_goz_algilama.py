import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

face_cascade=cv2.CascadeClassifier("C:\\udemyopencv\\haar_cascade\\haar_cascade_file\\frontalface.xml")
eye_cascade=cv2.CascadeClassifier("C:\\udemyopencv\\haar_cascade\\haar_cascade_file\\HaarCascade_eye.xml")

while 1:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(480,360))
    if _==False:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    roi_frame = frame[y:y + h, x:x + w]  # cızdıgım rectangle bolgesini aldım
    roi_gray = gray[y:y + h, x:x + w]

    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_frame, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)
    cv2.imshow("Eye", frame)

    if cv2.waitKey(30)&0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()