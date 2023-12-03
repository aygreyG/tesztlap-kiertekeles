""" 3. lépés """

# from transformers import pipeline
from enum import Enum
import pandas as pd
import re

class StringClass(Enum):
    Answer = "LABEL_0"
    Question = "LABEL_1"

class ClassificationSolution:
    def __init__(self, model = "shahrukhx01/question-vs-statement-classifier") -> None:
        self.classifier = None #pipeline("text-classification", model=model, tokenizer=model)
        pass
    
    def simplistic_classifier(self, sentence: str):
        # for simple solution. Just check if it has number and a dot. at the start
        is_numbered = bool(re.match(r'^\d+\.', sentence))
        if is_numbered:
            return StringClass.Question
        return StringClass.Answer


    
    def classify(self, sentence) -> StringClass:
        result = self.classifier(sentence)
        return StringClass(result[0]['label'])
    
    def algorithm(self, path = "tesztlap-kiertekeles/test_data/sentence_classification/S08_question_answer_pairs.txt"):
        self.test_data(path)
        pass
        
    def test_data(self, path) -> [[str], [str]]:
        df = pd.read_csv(path, sep='\t')
        questions_list = df['Question'].tolist()
        answer_list = df['Answer'].tolist()
        score = 0
        total = 0
        for x in range(len(questions_list)):
            print(questions_list[x])
            print(answer_list[x])
            if type(questions_list[x]) != str or type(answer_list[x]) != str:
                continue
            total += 1
            if self.simplistic_classifier(questions_list[x]) == StringClass.Question and self.simplistic_classifier(answer_list[x]) == StringClass.Answer:
                score += 1
        print("score:", score/total)
        return score/total

if __name__ == "__main__":
    ClassificationSolution().algorithm()
