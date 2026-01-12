import streamlit as st
import numpy as np
from PIL import Image
from tensorflow import keras

@st.cache_resource
def load_model():
    """
    load the pneumonia classifier model with caching
    so it doesnt load everytime the app is run
    """
    model = keras.models.load_model('oversampled_pneumonia_classifier.hdf5')
    return model


st.set_page_config(
    page_title="Chest X-ray classifier",
    page_icon="🩻",
)

#### SIDEBAR ####
st.sidebar.header("Upload an X-ray")
img_data = st.sidebar.file_uploader(
    label="Upload a chest X-ray image",
    type=['png', 'jpg'],
    label_visibility="collapsed"
)
st.sidebar.success("Check out the docs page for some X-ray images you can try with the model :)")

#### MAIN ####
st.header("Pneumonia Diagnosis")
st.write("""Upload an X-ray image using the sidebar to get a diagnosis.""")

if img_data is not None:
    uploaded_img = Image.open(img_data)
    
    # load model
    model = load_model()

    # preprocess image
    img = uploaded_img.convert('L')  
    img = img.resize((128, 128))  
    pixels = np.asarray(img)
    pixels = pixels.astype('float32')
    pixels /= 255.0
    pixels = np.expand_dims(pixels, axis=0)  
    pixels = np.expand_dims(pixels, axis=-1)  

    # generate prediction
    prediction = model.predict(pixels)
    
    # display result in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Uploaded X-ray")
        st.image(uploaded_img, use_container_width=True)
    
    with col2:
        st.subheader("Diagnosis Result")
        probability = prediction[0][0] * 100  
        
        if probability < 0.5:
            st.metric("Result", "Pneumonia 😦", border=True)
            st.metric("Probability", f"{(100 - probability):.1f}%", border=True)
        else:
            st.metric("Result", "Normal 😊", border=True)
            st.metric("Probability", f"{probability:.1f}%", border=True)