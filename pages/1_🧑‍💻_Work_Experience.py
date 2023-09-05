import streamlit as st

st.set_page_config(
    page_title="Work experience",
    page_icon="🧑‍💻",
)

st.title("Work experience.")

st.subheader('💻Artificial Intelligence Developer - Red Point')
st.markdown(
    """
     *4 months* 
    ##### Summary:
    I worked on testing and documenting various artificial 
    intelligence projects. Additionally, I contributed to the 
    implementation of computer vision algorithms for object 
    detection using heuristic techniques. I also assisted in 
    managing SQL databases and creating APIs with Flask.
    """
)

st.subheader('Tools used.')


col1, col2, col3 = st.columns(3)

with col1:
    st.write(
        """
        - Python
        - Pandas
        - Numpy
        - MySQL
        """
    )
with col2:
    st.write(
        """
        - AWS
        - Flask
        - APIs
        - Git / Github
        """
    )

with col3:
    st.write(
        """
        - Computer vision.
        - OpenCV
        - Pillow
        """
    )
    
    
    
st.subheader('🧠Neuroscience Research - CINVESTAV')
st.markdown(
    """
     *2 months* 
    ##### Summary:
    I worked in collaboration with PhD students researching 
    about the hippocampus, specifically Spike sorting. I 
    updated the tools used in the workflow and advanced the 
    analysis of the large volumes of data produced by the
    experiments in HDF5 format. As well as setting the direction 
    for the implementation of graphical interfaces to visualize 
    the data.
    """
)

st.subheader('Tools used.')


col1, col2, col3 = st.columns(3)

with col1:
    st.write(
        """
        - Python
        - Pandas
        - Numpy
        - Matplotlib
        """
    )
with col2:
    st.write(
        """
        - HDF5
        - Tkinter
        - Clustering
        """
    )

with col3:
    st.write(
        """
        - Julia
        - C
        - CUDA
        """
    )