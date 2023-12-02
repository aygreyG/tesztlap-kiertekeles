import readphoto
import sentence_classification
import detect_drawing


def main():
    test_images: list = []
    sections: list[list[dict]] = [] # a section should contain data_pieces. The a sentence (detected text) and an image of the text. The section should
    # sections = foo(test_images) # 1. lépés
    # sections = bar(test_images) # 2. lépés
    marked_answers: list[int] = [] # the marked answers for each section.
    for section in sections:
        classificator = sentence_classification.ClassificationSolution() # 3. lépés
        classificator.test_data(section)
        marked_anwer = 0
        for data_piece in section:
            sentence_type = classificator.classify(data_piece['sentence'])
            answers = []
            if sentence_type == sentence_classification.StringClass.Answer:
                answers.append(data_piece)
            detector = detect_drawing.DetectDrawingSolution()   # 4. lépés
            detected_type: detect_drawing.DrawingClass = detector.algorithm(data_piece['image']) # 
            if detected_type == detect_drawing.DrawingClass.MARKED:
                marked_answer = len(answers)
    # foo(marked_answers, test_images) # 5. lépés
    # bar(marked_answers, test_images) # 6. lépés

if __name__ == "__main__":
    main()
