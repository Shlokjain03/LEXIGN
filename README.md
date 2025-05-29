🧠 Sign Language Learning & Communication Assistant
--------------------------------------------------
A real-time AI-powered Flask web app for learning, recognizing, and communicating using Sign Language.
_______________________________________________________________________________

⚙️ Features
----------------------------------------------------------------------------------------------------
✋ Real-time Sign Language Recognition from webcam video using MediaPipe hand landmarks
🧠 Sign Classification powered by a trained RandomForest model
📚 Learn Mode with interactive flashcards and sign language videos
🗣️ Audio-to-Sign Translation (basic) with audio upload and video output
🌐 Clean Flask-based interface with multiple routes for different functionalities
_______________________________________________________________________________

🚀 Getting Started
-------------------------------------------------------------------------------

1️⃣ Clone the repository:
bash
Copy
Edit
git clone https://github.com/your-username/sign-language-assistant.git

cd sign-language-assistant
2️⃣ Install Python dependencies:
bash
Copy
Edit

pip install -r requirements.txt
3️⃣ Train the model (optional):
If model.p is not present, train the classifier:
bash
Copy
Edit
python train.py
This will use data.pickle to train the RandomForest model.

4️⃣ Run the app:
bash
Copy
Edit
python app.py

🌐 Visit in your browser:
http://127.0.0.1:5000/
_______________________________________________________________________________

🧰 Tech Stack & Tools
--------------------------------------------------
Python, Flask — Web backend framework
OpenCV, MediaPipe — Webcam capture & hand landmark detection
scikit-learn (RandomForestClassifier) — Sign classification model
NumPy, Pickle — Data handling & model persistence
HTML, CSS, JavaScript — Frontend UI
Flask Blueprints — Modular route management
_______________________________________________________________________________

📁 Project Data
--------------------------------------------------
data.pickle — Pickled hand landmark data for training
model.p — Trained RandomForest model (produced by train.py)
templates/ — HTML templates for pages like home, sign detection, learn mode, etc.
static/ — Static assets (CSS, JS, videos for learning mode)
routes/learn.py — Blueprint for Learn Mode features
_______________________________________________________________________________

🎯 Conclusion
----------------------------------------------------------------------------------------------------

This Sign Language Learning & Communication Assistant app offers an accessible way for users to learn and communicate with sign language through AI-powered real-time recognition and interactive learning resources. It is ideal for beginners, educators, and developers interested in combining computer vision, machine learning, and web technologies. Contributions and customizations are welcome to expand its functionality and improve accessibility!

