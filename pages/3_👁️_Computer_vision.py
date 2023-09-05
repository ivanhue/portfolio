import streamlit as st

st.set_page_config(
    page_title="Computer vision",
    page_icon="👁️",
)

st.markdown(
    """
    # Computer vision.
    
    ## Human Pose Detection.
    
    ### Summary.
    
    In human pose detection, accurate detection is crucial, 
    particularly in medical fields. That's why, during a 
    project in partnership with physiotherapists, we explored 
    ways to improve the accuracy of identifying movements that 
    doctors might recommend. After considering various options,
    we decided to implement the one euro filter. 
    
    As part of this effort, the project involved an extensive 
    research process in CNN, along with a document justifying 
    and explaining the operation of each tool used.
    
    ### Development.
    
    I conducted research on the history of artificial neural 
    networks, including CNNs, primarily based on David Marr's 
    book, "Vision" and the work by Yann LeCun on this architecture.
    I also explored the current state of the art in human pose 
    detection and, lastly, explored MediaPipe and its specific 
    application for this case.

    Following the research, I carried out tests on videos of 
    therapists performing exercises and examined how jittering 
    impacted accurate detection.

    With the assistance of a colleague, we ensured proper data 
    labeling for subsequent comparison between data with and without
    the filter.

    Ultimately, I performed testing and error calculations.
    
    ### Conclusions.
    
    In conclusion, the project exhibited improvement with the 
    filter; however, the processing speed noticeably decreased. 
    Depending on the application, for slow and controlled movements, 
    the filter yields substantial enhancement with minimal lag. On 
    the other hand, for quicker or abrupt motions, the detection 
    quality declined when the filter was applied.
    
    
    ## Working on more examples, plots, and projects...
    

    """
)