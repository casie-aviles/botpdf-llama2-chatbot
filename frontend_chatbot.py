import streamlit as st
from llm_interface import stream_response

if __name__ == "__main__":
    # Set app configurations
    st.set_page_config(page_title="Assistant Chatbot")
    st.title("🤖 Assistant Chatbot")
    st.caption("Streamlit chatbot powered by 🦙 Llama 2 LLM ")

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
