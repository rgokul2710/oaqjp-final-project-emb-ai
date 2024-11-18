import unittest
from EmotionDetection import emotion_detection

class TestEmotionDetector(unittest.TestCase) :

    def test_emotion_detector(self) :
        test_cases = [
            {"text": "I am glad this happened" , "expected_dominant_emotion" : "joy"},
            {"text": "I am really mad about this" , "expected_dominant_emotion" : "anger"},
            {"text": "I feel disgusted just hearing about this" , "expected_dominant_emotion" : "disgust"},
            {"text": "I am so sad about this" , "expected_dominant_emotion" : "sadness"},
            {"text": "I am really afraid that this will happen" , "expected_dominant_emotion" : "fear"}
        ]
        for case in test_cases:
            result = emotion_detection.emotion_detector(case['text'])
            dominant_emotion = result.get('dominant_emotion')
            self.assertEqua1(dominant_emotion, case['expected_dominant_emotion'],
                    f"Failed for input: '{case['text']}'")
            print(f"Text: '{case['text']}' -> Dominant Emotion: '{dominant_emotion}'")

if __name__ == "__main__" : 
    unittest.main()