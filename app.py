from flask import Flask, render_template, request, Response
import cv2
import mediapipe as mp
import numpy as np
from classifier import SignLanguageClassifier
from routes.learn import learn, flashcards, videos

app = Flask(__name__, static_url_path='/static')

# === Register Blueprint ===
app.register_blueprint(learn, url_prefix='/learn')

# === Initialize Sign Language Classifier ===
classifier = SignLanguageClassifier('model.p')

# === Initialize MediaPipe ===
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

# === Initialize Webcam ===
cap = cv2.VideoCapture(0)

# === Webcam Frame Generator ===
def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break

        H, W, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        data_aux = []
        all_x, all_y = [], []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

                x_, y_ = [], []
                for lm in hand_landmarks.landmark:
                    x_.append(lm.x)
                    y_.append(lm.y)
                    all_x.append(lm.x)
                    all_y.append(lm.y)

                min_x = min(x_)
                min_y = min(y_)

                for lm in hand_landmarks.landmark:
                    data_aux.append(lm.x - min_x)
                    data_aux.append(lm.y - min_y)

            try:
                x1 = int(min(all_x) * W) - 20
                y1 = int(min(all_y) * H) - 20
                x2 = int(max(all_x) * W) + 20
                y2 = int(max(all_y) * H) + 20

                prediction = classifier.predict(data_aux)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                cv2.putText(frame, prediction, (x1, y1 - 15), cv2.FONT_HERSHEY_SIMPLEX,
                            1.2, (0, 255, 0), 3, cv2.LINE_AA)

            except Exception as e:
                cv2.putText(frame, "Prediction Error", (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                            1.0, (0, 0, 255), 2, cv2.LINE_AA)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# === ROUTES ===

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/audio', methods=['GET', 'POST'])
def audio():
    transcript = None
    video_file = None

    if request.method == "POST":
        if "audio_data" not in request.files:
            transcript = "No audio file uploaded."
        else:
            audio_file = request.files["audio_data"]
            if audio_file.filename == "":
                transcript = "No audio file selected."
            else:
                # Dummy audio-to-text result
                transcript = "hello"
                video_file = "hello.mp4"

    return render_template("text.html", transcript=transcript, video_file=video_file)

@app.route('/flashcards')
def flashcard_view():
    return render_template('learn.html', flashcards=flashcards, videos=videos)

@app.route('/videos')
def video_view():
    return render_template('learn.html', flashcards=flashcards, videos=videos)

@app.route('/learn_all')
def learn_all():
    return render_template('learn.html', flashcards=flashcards, videos=videos)

if __name__ == '__main__':
    app.run(debug=True)
