import youtube_assistant as ya
import streamlit as st

st.title("Youtube Assistant")
st.write("This is a simple youtube assistant that can help you generate a video title and description")

if "messages" not in st.session_state:
    st.session_state.messages= []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if user_input := st.chat_input("Tell me about your video?"):

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    #generate response
    response = ya.youtube_assistant(user_input)

    #display response
    with st.chat_message("assistant"):
       st.markdown(response)

    # Add user message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})








