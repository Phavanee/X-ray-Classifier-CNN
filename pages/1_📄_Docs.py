import streamlit as st

st.set_page_config(page_title="Documentation", page_icon="📄")
st.sidebar.success("Made with ❤️ by :\n\n1. Phavanee Katriya\n2. Amelia Adlina\n3. Athirah Syafiqah\n4. Aina Syafina")

st.title('Docs')
st.write(
    """Writing a little bit about the model and the app because a lot of work went into it!!!"""
)

st.header("The Problem")
st.write("""
    The main problem this project aims to solve is providing a very simple front end for healthcare 
    practitioners to upload a chest X-ray image, and get a diagnosis result (of course, we cannot 
    diagnose anything other than pneumonia, but it's a fun start!!).
    """)

st.header("The Model")
st.write("""
    The model is a convolutional neural network (CNN) built from scratch. Our group trained it on 
    a dataset obtained from Kaggle, authored by Paul Mooney. If you came here for some X-rays to use, 
    here you go:
""")


st.header("X-ray samples")

with st.container(border=True) :
    st.subheader("Normal X-rays")
    scol1, scol2, scol3 = st.columns(3)
    with scol1:
        st.image('./xrays/norm-norm.jpeg')
    with scol2:
        st.image('./xrays/norm-kindapneum.jpeg')
    with scol3:
        st.image('./xrays/norm-vpneum.jpeg')
    with st.expander("Why we chose these images:"):
        st.write("""
        1. The first image is a normal X-ray that looks like a normal X-ray.
        \n2. The second image is normal X-ray that kiiind of looks like it may have pneumonia.
        \n3. The third image is a really looks like it might be pneumonia.
        \n*all these judgements are made by someone who has seen a lot of X-rays this semester
        \n*a doctor might think otherwise
        """)

with st.container(border=True) :
    st.subheader("Pneumonia X-rays")
    scol1, scol2, scol3 = st.columns(3)
    with scol1:
        st.image('./xrays/pneum-pneum.jpeg')
    with scol2:
        st.image('./xrays/pneum-kindanorm.jpeg')
    with scol3:
        st.image('./xrays/pneum-vnorm.jpeg')
    with st.expander("Why we chose these images:"):
        st.write("""
        1. The first image is a pneumonia X-ray that looks like pneumonia.
        \n2. The second image is pneumonia X-ray that sorta looks normal.
        \n3. The third image is a pneumonia X-ray that looks like it might be normal.
        \n*all these judgements are made by someone who has seen a lot of X-rays this semester
        \n*a doctor might think otherwise
        """)


st.header("Special Thanks")
st.write("""
    1. Dr. Chan, for teaching us and letting us have fun with this project.
    2. Tyler-Simons, his app layout made me realize you can use the sidebar to upload images. The app 
    would've looked so bad if I hadn't known that. (https://github.com/tyler-simons)
    """)