import streamlit as st
import pandas as pd
import numpy as np
st.title('Steak Doneness Classifier')

add_selectbox = st.sidebar.write(
    'Steak Doneness Classifier'
)

add_selectbox = st.sidebar.image(
    'https://i.pinimg.com/originals/41/4e/57/414e57ac74d11b5bba0632f16a560589.jpg',
    use_column_width=True
)

add_selectbox = st.sidebar.write(
    'This web appliaction can predict the doneness of a steak via image input. The doneness of steak ranges from rare to well done!'
)

add_selectbox = st.sidebar.write(
    'Streamlit [link](https://share.streamlit.io/thetrapperxd/steakdonenessclassifier/main/steak_doneness_classifier.py)',
)

add_selectbox = st.sidebar.write(
    'Google Collab [link](https://colab.research.google.com/drive/10Ou7pwsSA-b71ho2SntqZy840U7j4qCJ#scrollTo=VUTA5XB-M_O2)',
)

add_selectbox = st.sidebar.write(
    'Github [link](https://github.com/TheTrapperXD/steakdonenessclassifier)',
)

add_selectbox = st.sidebar.write(
    'Kaggle Dataset [link](https://www.kaggle.com/datasets/pattanunw/steak-doneness-alternate)',
)

add_selectbox = st.sidebar.write(
    'Reddit [link](https://www.reddit.com/user/TheTrapperBeingXD)',
)

 
from fastai.vision.widgets import *
from fastai.vision.all import *

from pathlib import Path

import streamlit as st

class Predict:
    def __init__(self, filename):
        self.learn_inference = load_learner(Path()/filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()
    
    @staticmethod
    def get_image_from_upload():
        st.image('https://staticfanpage.akamaized.net/wp-content/uploads/sites/22/2020/07/shutterstock_706040446.jpg',
        use_column_width=True)
        st.write("This web appliaction can predict the doneness of a steak via image input. The doneness of steak ranges from rare to well done!")
        st.write("Steak Doneness Scale")
        st.write("01-rare")
        st.write("02-mediumrare")
        st.write("03-medium")
        st.write("04-mediumwell")
        st.write("05-well")
        uploaded_file = st.file_uploader("Upload an image file to classify the steak doneness!",type=['png','jpeg', 'jpg'])
        if uploaded_file is not None:
            return PILImage.create((uploaded_file))
        return None

    def display_output(self):
        st.image(self.img.to_thumb(500,500), caption='Uploaded Image')

    def get_prediction(self):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            st.write(f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}')

if __name__=='__main__':

    file_name='steakdonenessclassifier.pkl'

    predictor = Predict(file_name)
