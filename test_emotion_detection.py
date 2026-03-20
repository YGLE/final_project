from EmotionDetection.emotion_detection import emotion_detector  # Import the emotion_detection module

def test_emotion_detection():
    texts = [
        "I am glad this happened.",
        "I am really mad about this.",
        "I feel disgusted just hearing about this.",
        "I am so sad about this.",
        "I am really afraid that this will happen"
    ]

    for text in texts:
        print(f"Testing with text: {text}")
        result = emotion_detector(text)
        print(f"Emotion Response: {result}\n")

if __name__ == "__main__":
    test_emotion_detection()