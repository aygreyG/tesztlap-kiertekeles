import numpy as np
import cv2
import pytesseract


#Beolvassa a megoldásokat.
#esetlegesen módosítani az elérési utat.
with open('megol.txt') as f:
        contents=[line.strip() for line in f.readlines()]
#Listák létrehozása, bennük tárolt szöveg kisbetűsre alakítása
solved=contents
#A kitöltő által adott válaszok stringeket tárol.
#anwsers-be kell bekötni a detektált válaszokat
anwsers= ["0","2"]
sol=np.array(solved)
anw=np.array(anwsers)
anw1=[]
good=[]
#átalakító, hogy a pontszámot könnyedén kiszámolja
for s in range(0,anw.size):
    if(anw[s]=="0"):
        anw1.append("a")
    if(anw[s]=="1"):
        anw1.append("b")
    if (anw[s] == "2"):
        anw1.append("c")
    if (anw[s] == "3"):
        anw1.append("d")
anw2=np.array(anw1)
#pontszám számoló ha nem egyenlő a számuk 0-ad.
if(sol.size==anw2.size):
  for i in range(0,anw2.size):
    if(sol[i]==anw2[i]):
     good.append(anw2[i])
#maximálispontszám
maxpont= len(solved)
#elért pontszám
pontszam=len(good)

#keretézés
#itt kell módosítani a kép elérési útját.
original_image = cv2.imread("sheet_01.jpg")
gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

#végig fut az általunk megadott válaszokon
for st in anw1:
  target_text = st
  df = pytesseract.image_to_data(gray, "eng", "--psm 6", output_type=pytesseract.Output.DATAFRAME)
  for line_num, words_per_line in df.groupby("line_num"):
    words_per_line = words_per_line[words_per_line["conf"] >= 70]
    if not len(words_per_line):
        continue

    words = words_per_line["text"].values
    #minden sorban lévő szót összefűz.
    line = " ".join(words)
    lowline=line.lower()
    #ha a keresett szó szerepel a sorban bekeretezi, annak függvényében, hogy a jó válaszok között van-e vagy sem.
    if target_text in lowline:
        if(st in good):
            word_boxes = []
            for left, top, width, height in words_per_line[["left", "top", "width", "height"]].values:
                    word_boxes.append((left, top))
                    word_boxes.append((left + width, top + height))

            x, y, w, h = cv2.boundingRect(np.array(word_boxes))
            cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if(st not in good):
            word_boxes = []

            for left, top, width, height in words_per_line[["left", "top", "width", "height"]].values:
                    word_boxes.append((left, top))
                    word_boxes.append((left + width, top + height))

            x, y, w, h = cv2.boundingRect(np.array(word_boxes))
            cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
#A képre kiírja a pontszámot.
cv2.putText(original_image, "Pontszam: %d/%d"%(pontszam,maxpont), (300, 20), 1, 1, (0, 0, 255), 1)
cv2.imshow('image', original_image)
key=cv2.waitKey(0)