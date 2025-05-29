import os
import pickle
import mediapipe as mp
import cv2
import time

# --- Part 1: Data Collection ---

CLASSES = ['hello','thanks','iloveu','yes','no','bathroom','play']
DATA_DIR = './data'
dataset_size = 5  # Number of images per word

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

cap = cv2.VideoCapture(0)

for word in CLASSES:
    word_path = os.path.join(DATA_DIR, word)
    os.makedirs(word_path, exist_ok=True)

    print(f'Collecting data for word: {word}')

    # Wait for user to press 'q' to begin capturing for this word
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, f'Ready to capture: "{word.upper()}" - Press "Q"', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Capture with 2-second delay + countdown for each image
    for counter in range(dataset_size):
        for countdown in range(3, 0, -1):  # 3-second countdown
            ret, frame = cap.read()
            if not ret:
                continue
            cv2.putText(frame, f'Capturing in {countdown}', (200, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4, cv2.LINE_AA)
            cv2.imshow('frame', frame)
            cv2.waitKey(1000)  # 1 second per countdown step

        ret, frame = cap.read()
        if ret:
            img_path = os.path.join(word_path, f'{counter}.jpg')
            cv2.imwrite(img_path, frame)
            print(f"Saved: {img_path}")
            # Optional: show confirmation
            cv2.putText(frame, f'Saved {counter+1}/{dataset_size}', (50, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            cv2.imshow('frame', frame)
            cv2.waitKey(500)  # Brief pause before next countdown

cap.release()
cv2.destroyAllWindows()

# --- Part 2: Extract Landmarks with MediaPipe ---

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

data = []
labels = []

for dir_ in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, dir_)
    if not os.path.isdir(dir_path):
        continue

    for img_name in os.listdir(dir_path):
        img_path = os.path.join(dir_path, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                x_coords = [lm.x for lm in hand_landmarks.landmark]
                y_coords = [lm.y for lm in hand_landmarks.landmark]

                data_aux = []
                min_x, min_y = min(x_coords), min(y_coords)

                for lm in hand_landmarks.landmark:
                    data_aux.append(lm.x - min_x)
                    data_aux.append(lm.y - min_y)

                data.append(data_aux)
                labels.append(dir_)

# Save the extracted features
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)

print(f"✅ Data collection complete. Total samples: {len(data)}")
