import pickle
import numpy as np

class SignLanguageClassifier:
    def __init__(self, model_path='model.p'):
        model_dict = pickle.load(open(model_path, 'rb'))
        self.model = model_dict['model']

    def predict(self, landmarks):
        """
        Predicts the sign language class from the landmarks
        """
        return self.model.predict([np.asarray(landmarks)])[0]
