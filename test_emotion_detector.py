from emotion_detection import emotion_detector  # Import the emotion_detection module

def test_emotion_detection():
    texts = [
        "I hate bananas. Bananas are bad.",
        "I am feeling very happy today.",
        "This is a sad day.",
        "I'm not sure how I feel right now."
    ]

    for text in texts:
        print(f"Testing with text: {text}")
        result = emotion_detector(text)
        print(f"Emotion Response: {result}\n")

if __name__ == "__main__":
    test_emotion_detection()