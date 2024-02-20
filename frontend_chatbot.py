import os
import streamlit as st
from llm_interface import stream_response

def save_uploaded_file(uploaded_file):
    """
    Saves an uploaded file to a specified directory.

    Args:
        uploaded_file: Uploaded file object to be saved.

    Returns:
        An acknowledgment message upon successful saving of the file.

    Raises:
        Any exceptions raised during the file saving process.

    Note:
        This function assumes the existence of a 'data' directory in the current working directory.
        If the directory does not exist, an appropriate exception will be raised.
    """
    with open(os.path.join("data", uploaded_file.name), "wb") as file:
        file.write(uploaded_file.getbuffer())
    return st.success(f"Saved PDF file: {uploaded_file.name} to directory")

if __name__ == "__main__":
    # Set app configurations
    st.set_page_config(page_title="Assistant Chatbot")
    st.title("🤖 Assistant Chatbot")
    st.caption("Streamlit chatbot powered by 🦙 Llama 2 LLM ")

    # Add sidebar for file upload feature
    st.sidebar.title("📤 Upload PDF")
    uploaded_pdf = st.sidebar.file_uploader("Have the assistant take a look at your PDF file", type=["pdf"])

    # Save the file once uploaded
    if uploaded_pdf is not None:
        save_uploaded_file(uploaded_pdf)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    # Display messages from chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Accept user input
    if prompt := st.chat_input():
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        st.chat_message("user").write(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            with st.spinner("Generating..."):
                response = st.write_stream(stream_response(prompt))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
