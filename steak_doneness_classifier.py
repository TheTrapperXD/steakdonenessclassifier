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
    'Links [link]()',
)

add_selectbox = st.sidebar.write(
    'Google Collab [link]()',
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

 
import pandas as pd
from PIL import Image 


from enum import Enum
from io import BytesIO, StringIO
from typing import Union

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""


class FileUpload(object):

    def __init__(self):
        self.fileTypes = ["png", "jpg"]

    def run(self):
        """
        Upload File on Streamlit Code
        :return:
        """
        st.info(__doc__)
        st.markdown(STYLE, unsafe_allow_html=True)
        file = st.file_uploader("Upload file", type=self.fileTypes)
        show_file = st.empty()
        if not file:
            show_file.info("Please upload a file of type: " + ", ".join(["png", "jpg"]))
            return
        content = file.getvalue()
        if isinstance(file, BytesIO):
            show_file.image(file)
        else:
            data = pd.read_csv(file)
            st.dataframe(data.head(10))
        file.close()


if __name__ ==  "__main__":
    helper = FileUpload()
    helper.run()
    
from fastai.vision.widgets import *
from fastai.vision.all import *

from pathlib import Path

import streamlit as st


def label_func(f):
    return f[0].isupper()


class Predict:
    def __init__(self, filename):

        self.learn_inference = load_learner(Path() / filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()

    @staticmethod
    def get_image_from_upload():
        uploaded_file = st.file_uploader("Upload Files", type=["png","jpg"])
        if uploaded_file is not None:
            return PILImage.create((uploaded_file))
        return None

    def display_output(self):
        st.image(self.img.to_thumb(500, 500), caption="Uploaded Image")

    def get_prediction(self):

        if st.button("Classify"):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            st.write(f"Prediction: {pred}; Probability: {probs[pred_idx]:.04f}")
        else:
            st.write(f"Click the button to classify")


if __name__ == '__main__':

    file_name = "steak_doneness_classifier.pth"

    predictor = Predict(file_name)
