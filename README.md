# Tech Stack
- [`streamlit`](https://streamlit.io/) - frontend
- [`ollama`](https://ollama.com/) - run open-source LLMs locally
    - [`llama2`](https://huggingface.co/blog/llama2) - LLM
- [`llama_index`](https://www.llamaindex.ai/) - RAG framework
- [`chromadb`](https://www.trychroma.com/) - vector database

# Setup
After cloning the repository, follow the steps below to install the dependencies and run the app:
- Run `pip install -r requirements.txt`
- Download and install [`ollama`](https://ollama.com/download)
- Run `ollama pull llama2`
- Run `ollama serve`
- Run `streamlit run frontend_chatbot.py` in the command line