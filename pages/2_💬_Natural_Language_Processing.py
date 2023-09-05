import streamlit as st

st.set_page_config(
    page_title="Chatbot",
    page_icon="💬",
)


# st.title("""""")

st.markdown(
    """
    # Natural Language Processing.
    
    ## Answer questions about your own data using RASA and Langchain.
    
    ### Summary.

    We aimed to automate the process of addressing frequently asked 
    questions from students using a chatbot. Due to resource 
    limitations, we employed lightweight tools such as Langchain, 
    RASA, TF-IDF, and Python. To gather the necessary data, we 
    utilized a web crawler.
    
    """
)

st.image(
    "images/chatbot-architecture.jpeg", 
    caption="Chatbot architecture.",
    use_column_width=True
)


st.markdown(
    """  
    ### Creating the [dataset](https://github.com/ivanhue/scraping_urls).
    
    The information used for this model was gathered from university 
    websites using regex rules and asyncio for the performance. 
    The scraping focused on two types of formats: PDF files and 
    plain text from websites. Keywords, preprocessed website text,
    and URLs were extracted. Finally, the results were filtered and 
    saved in JSON format, with the option to store them in a SQL 
    database in the future.
    
    
    ### Creating the retriever.
    
    For information retrieval, each document was vectorized 
    using TF-IDF with focus on Spanish configurations. 
    Then, we saved an instance of the model that was created 
    using these vectors. To find the most similar documents, we 
    vectorized the query and used cosine similarity.
    
    """
)
    
st.image(
    "images\query-vector.png", 
    caption="Query vector.",
    use_column_width=True
)

st.markdown(
    """
    
    ### Answering questions.
    
    We employed RASA to train a model that identifies user 
    questions and generates predefined answers based on the 
    query type. Additionally, the model provides the user with 
    the most relevant web pages.
    
    """
)
    
st.image(
    "images\documents.png", 
    caption="documents cosine similarity distance.",
    use_column_width=True
)

st.markdown(
    """
    
    ### Conclusions.
    
    TF-IDF performance tests showed promising results in document 
    filtering. It's important to evaluate the dataset's quality 
    used for training and to review the tokenizer. Additionally, 
    if more resources become available, potential enhancements 
    include implementing a large language model for generating 
    answers based on the retrieved documents.
    
    
    """
)
    
st.image(
    "images/all-documents.png", 
    caption="Using PCA to visualize the documents.",
    use_column_width=True
)

st.markdown(
    """
    
    
    ## Working on more examples, plots, and projects...
    
    
    
    
    """
)

