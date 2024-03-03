# 🤖BotPDF
A Large Language Model (LLM) chatbot project, where users can upload PDF files to receive tailored responses generated directly from the document contents.

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

# Demo
## Upload your PDF
https://github.com/casie-aviles/botpdf-llama2-chatbot/assets/80239105/3185a3d4-36c9-41e4-8da0-cba8f1dde633
## Ask away
https://github.com/casie-aviles/botpdf-llama2-chatbot/assets/80239105/27717982-ced6-4ba3-921f-64191210a9fd
## Multiple uploads
https://github.com/casie-aviles/botpdf-llama2-chatbot/assets/80239105/94a2f3a8-d296-4a1f-94cc-69d2447f7fa6
## Cross-reference your PDFs
https://github.com/casie-aviles/botpdf-llama2-chatbot/assets/80239105/2c76dba5-a654-43ae-b6c0-31f6621584fa




