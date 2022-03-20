import cv2
#gozzleri bulmak icin yuz haar cascade kullanaagız yuzdeki gozleri bulacagız:)
img=cv2.imread("C:\\udemyopencv\\haar_cascade\\test_images\\face.png")
face_cascade=cv2.CascadeClassifier("C:\\udemyopencv\\haar_cascade\\haar_cascade_file\\frontalface.xml")
eye_cascade=cv2.CascadeClassifier("C:\\udemyopencv\\haar_cascade\\haar_cascade_file\\HaarCascade_eye.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.3,5)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
img2=img[y:y+h,x:x+w]#cızdıgım rectangle bolgesini aldım
gray2=gray[y:y+h,x:x+w]

eyes=eye_cascade.detectMultiScale(gray2,1.3,5)

for(ex,ey,ew,eh) in eyes:
    cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
cv2.imshow("Eye",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#NOT:img2 yi img nin içindeki koordinatlar ile tanımladık yani
# img2 yi bir nevi roi belirledik gibi düşünebilirsin. O yüzden karelerin hepsi img içerisinde gözüküyor.