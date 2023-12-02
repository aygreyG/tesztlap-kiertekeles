""" 3. lépés """

from transformers import pipeline
from enum import Enum
import pandas as pd

class StringClass(Enum):
    Answer = "LABEL_0"
    Question = "LABEL_1"

class ClassificationSolution:
    def __init__(self, sentences: list[str], model = "shahrukhx01/question-vs-statement-classifier") -> None:
        self.classifier = pipeline("text-classification", model=model, tokenizer=model)
    
    def classify(self, sentence) -> StringClass:
        result = self.classifier(sentence)
        return StringClass(result[0]['label'])
    
    def algorithm(self, path = "S08_question_answer_pairs.txt"):
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
            if self.classify(questions_list[x]) == StringClass.Question and self.classify(answer_list[x]) == StringClass.Answer:
                score += 1
        print("score:", score/total)
        return score/total

if __name__ == "__main__":
    ClassificationSolution().algorithm()
