import os, cv2
import numpy as np
from PIL import Image

def Capture(regno,nos):
    cam = cv2.VideoCapture(1)
    Num = 0
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    path = "stud"+regno
    try:
        os.mkdir(path)
    except:
        while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    Num += 1
                    cv2.imwrite(f"{path}/{regno}_{Num}_.jpg",gray[y : y + h, x : x + w],)
                    cv2.imshow("Capturing", img)
                if cv2.waitKey(200) & 0xFF == ord("q"):
                    break
                elif Num > nos:
                    break
    cam.release()
    cv2.destroyAllWindows()
    TrainImage(regno,path)
    
def TrainImage(regno,path):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces, Id = getImages(path)
    recognizer.train(faces, np.array(Id))
    recognizer.save(f"TrainedModel/{regno}_Trainner.yml")
    print = "Trained"

def getImages(path):
    imagePath = [os.path.join(path, d) for d in os.listdir(path)]
    faces = []
    Ids = []
    for imagePath in imagePath:
        pil = Image.open(imagePath).convert("L")
        imageNp = np.array(pil, "uint8")
        Id = int(os.path.split(imagePath)[-1].split("_")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids

def check(paths):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(paths)
    facecasCade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cam = cv2.VideoCapture(1)
    frameCount=0
    while True:
            ___, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = facecasCade.detectMultiScale(gray, 1.2, 5)
            font = cv2.FONT_HERSHEY_SIMPLEX
            for (x, y, w, h) in faces:
                Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
                if conf > 30:
                    frameCount+=1
                    if frameCount == 10:
                        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                        cv2.imwrite(f"22bce8345_attendence_.jpg",im)
                        print("Attendance Noted")
                        break
                else:
                    Id = "?"
                    cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                    cv2.putText(im, Id, (x + h, y), font, 1, (0, 25, 255), 4)
            cv2.imshow("cheking",im)
            if cv2.waitKey(20) & 0xFF == ord("q"):
                break