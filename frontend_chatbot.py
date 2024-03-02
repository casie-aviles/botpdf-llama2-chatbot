import os
import time
import streamlit as st
from llm_interface import stream_response, search_pdf

def save_uploaded_file(uploaded_file):
    """
    Saves an uploaded file to a specified directory.

    Args:
    - uploaded_file: Uploaded file object to be saved.

    Returns:
    - An acknowledgment message upon successful saving of the file.

    Raises:
    - Any exceptions raised during the file saving process.

    Notes:
    - This function assumes the existence of a 'data' directory in the current working directory.
    - If the directory does not exist, an appropriate exception will be raised.
    """
    with open(os.path.join("data", uploaded_file.name), "wb") as file:
        file.write(uploaded_file.getbuffer())
    return st.sidebar.success(f"Saved PDF file: {uploaded_file.name} to directory")

def main():
    """
    Set app configurations and handle PDF upload, chat history, and user assistant interaction.
    """
    # Set app configurations
    st.set_page_config(page_title="BotPDF", page_icon="🤖")
    st.title("🤖 BotPDF")
    st.caption(body=
        """
        A streamlit chatbot powered by 🦙 Llama2 
        <acronym title="Large Language Model">LLM</acronym> with simple 
        <acronym title="Retrieval Augmented Generation">RAG</acronym>.
        """,
        unsafe_allow_html=True)
    st.divider()

    if os.path.exists('data') is False:
        os.mkdir('data')

    # Add sidebar with PDF uploader
    st.sidebar.title("📤 Upload PDF")
    st.sidebar.caption("Have the assistant take a look at your PDF file")
    uploaded_pdf = st.sidebar.file_uploader(label="label",
                                            label_visibility="collapsed",
                                            type=["pdf"])

    # Save the file once uploaded
    if uploaded_pdf is not None:
        save_uploaded_file(uploaded_pdf)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?", "elapsed_time": 0}]

    # Display messages from chat history
    for msg in st.session_state.messages:
        if msg["role"] == "assistant":
            st.chat_message(msg["role"]).write(msg["content"])
            st.caption(f"elapsed time: {msg['elapsed_time']}s")
        else:
            st.chat_message(msg["role"]).write(msg["content"])

    # Accept user input
    if prompt := st.chat_input():
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        st.chat_message("user").write(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            start_time = time.time()
            with st.spinner("Generating..."):
                if len(os.listdir('data/')) == 0:
                    # If no PDFs are uploaded, generate response without querying PDF
                    response = st.write_stream(stream_response(prompt))
                else:
                    # If PDFs are uploaded, query the PDFs
                    response = st.write_stream(search_pdf(prompt))
            end_time = time.time()
            elapsed_time = end_time - start_time
            elapsed_time = round(elapsed_time, 2)
        # Display LLM's elapsed time
        st.caption(f"elapsed time: {elapsed_time}s")
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response, "elapsed_time": elapsed_time})

if __name__ == "__main__":
    main()
