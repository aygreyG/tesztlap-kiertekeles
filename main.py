import readphoto
import sentence_classification
import detect_drawing
import os
import cv2
import pont_keret
import sys


def test_1_2():
    # TODO test
    test_images: list = []
    all_files = os.listdir('tesztlap-kiertekeles\\test_data\\drawing_detection')
    image_files = [file for file in all_files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    images = []
    for image_file in image_files:
        image_path = os.path.join('tesztlap-kiertekeles\\test_data\\drawing_detection', image_file)
        image = cv2.imread(image_path)
        images.append(image)
    sections = [
        ("62. asdasd asdasd", images[0], (0,0,0,0)),
        ("overloaded", images[0], (0,0,0,0)),
        ("floating", images[1], (0,0,0,0)),
        ("enlightened", images[2], (0,0,0,0)),
        ("lighted", images[3], (0,0,0,0)),
    ]
    return sections
    

def GT(sections: list[list[dict]] = []) -> list[int]: # INPUT (TEXT, IMAGE, COORDINATES) -> OUTPOUT (NUMBERS OF )
    marked_answers: list[int] = [] # the marked answers for each section.
    i = 0
    for index, section in enumerate(sections):
        classificator = sentence_classification.ClassificationSolution() # 3. lépés
        sentence_type = classificator.simplistic_classifier(section[0])
        answers = []
        marked_answer = None
        if sentence_type == sentence_classification.StringClass.Answer:
            answers.append(section)
        else:
            i = 0
            continue
        detector = detect_drawing.DetectDrawingSolution()   # 4. lépés
        detected_type: detect_drawing.DrawingClass = detector.algorithm(section[1]) #
        if detected_type == detect_drawing.DrawingClass.MARKED:
            marked_answer = index%4
            marked_answers.append(marked_answer)
        if index%5 == 4 and not marked_answer:
            marked_answer = 0
            marked_answers.append(marked_answer)
        i += 1
    print(marked_answers, len(marked_answers))
    return marked_answers

def main():
    if len(sys.argv) != 5:
        image_path = r'D:\project\egyetem\kepfel\tesztlap-kiertekeles\test_data\sheet_07.jpg'
        solution_path = r'D:\project\egyetem\kepfel\tesztlap-kiertekeles\Megol.txt'
        tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    else:
        image_path = sys.argv[2]
        solution_path = sys.argv[3]
        tesseract_path = sys.argv[4]
    sections = readphoto.get_regions(image_path, tesseract_path)
    marked_answers = GT(sections)
    val = pont_keret.pontszam(text_path=solution_path, anwsers_det=marked_answers)
    pont_keret.keret(img_path=image_path, ret=val)

if __name__ == "__main__":
    main()
