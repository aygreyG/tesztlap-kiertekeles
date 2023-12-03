import readphoto
import sentence_classification
import detect_drawing
import os
import cv2
import pont_keret


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
    for index, section in enumerate(sections):
        classificator = sentence_classification.ClassificationSolution() # 3. lépés
        sentence_type = classificator.simplistic_classifier(section[0])
        answers = []
        marked_answer = None
        if sentence_type == sentence_classification.StringClass.Answer:
            answers.append(section)
        detector = detect_drawing.DetectDrawingSolution()   # 4. lépés
        detected_type: detect_drawing.DrawingClass = detector.algorithm(section[1]) #
        if detected_type == detect_drawing.DrawingClass.MARKED:
            marked_answer = len(answers)
            marked_answers.append(marked_answer)
        if index%5 == 4 and not marked_answer:
            marked_answer = 0
            marked_answers.append(marked_answer)
    print(marked_answers)
    return marked_answers

def main():
    img_folder_path = r'tesztlap-kiertekeles\test_data'
    solution_path = r'tesztlap-kiertekeles\Megol.txt'
    sections = readphoto.get_regions(img_folder_path)
    marked_answers = GT(sections)
    # pont_keret.pontszam(text_path=solution_path, anwsers_det=marked_answers)
    # pont_keret.keret(img_path=img_folder_path)

if __name__ == "__main__":
    main()
