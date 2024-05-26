import youtube_assistant as ya
import streamlit as st
import time

st.title("A/L Youtube Assistant")
st.write("""This is a simple youtube assistant that can answer questions about videos you provide.
            Enter the Url of the video and click SUBMIT then ask any question about the video.
            The assistant will provide an answer based on the video's transcript.""")

if "messages" not in st.session_state:
    st.session_state.messages= []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get video URL from user
with st.sidebar:
    with st.form(key="video_url_form",clear_on_submit=True):
        submit_button = st.form_submit_button(label="Submit")
        video_url = st.sidebar.text_area(label="Enter the URL of the video",max_chars=100)

        

# React to user input
user_input= st.chat_input("Ask me about the video?")

if user_input and video_url :

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    #generate response
    db = ya.create_vector_db_from_youtube(video_url)
    response = ya.youtube_assistant(user_input,db)

    def stream_output():
     for word in response.split(" "):
        yield word + " "
        time.sleep(0.02)

    #display response
    with st.chat_message("assistant"):
       #st.markdown(response)
       st.write_stream( stream_output())

    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})









