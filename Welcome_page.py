import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

st.title("Alejandro Villegas.")

st.markdown('##### Machine learning and Data science')

st.write("Welcome to my portfolio website. Here you can find some of the projects I've worked on.")


st.subheader('About me.')
st.markdown(
    """
    Hello. I studied computer science at UAM-I focusing on machine learning and datascience.
    I really enjoy making tech solutions for real problemas. My favorite topics are 
    computer vision and natural language proccessing, and I want to learn more about RL.
    I wish be able to help in many projects and share my knowledge with the community of 
    artificial intelligence.
    """
)


st.subheader('Technical skills.')


col1, col2, col3 = st.columns(3)

with col1:
    st.write(
        """
        - Python
        - Pandas
        - Numpy
        - Matplotlib
        - SQL
        - Git / Github
        - Stadistics
        - Calculus
        
        """
    )
with col2:
    st.write(
        """
        - Natural language processing
        - Langchain
        - RASA
        - Words and documents embedding
        - Pytorch
        - Linear algebra
        - Docker
        """
    )

with col3:
    st.write(
        """
        - Computer vision.
        - OpenCV
        - Pillow
        - Mediapipe
        - Convolutional neural networds
        - SCRUM
        """
    )


st.markdown(
    """
    ##### 👈 Select a **topic** from the dropdown on the left to see what I have already done!
    """)


st.subheader('Soft skills.')

col21, col22, col23 = st.columns(3)


with col21:
    st.write(
        """
        - Communication
        - Adaptability
        - Work ethic
        """
    )
with col22:
    st.write(
        """
        - Creativity
        - Problem solving
        - Empathy
        """
    )

with col23:
    st.write(
        """
        - Leadership
        - Teamwork
        - Curiosity
        """
    )