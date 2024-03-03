# 🤖BotPDF
A simple Large Language Model (LLM) chatbot project, where users can upload PDF files to receive tailored responses generated directly from the document contents. Built using open-source tools and technologies in a controlled, local environment since not a lot of people have access to OpenAI API keys and other paid options. This is also to eliminate reliance on cloud services and provide an easier local set-up that should just work.

# What I learned
- How to use other forms of input for the LLM other than text prompts
- How we can customize context for the LLM via Retrieval Augmented Generation (RAG) without having to train your own LLM
- How RAG works by utilizing vector embeddings, which is a way to represent the semantics of words in a numerical form
- How to build a RAG pipeline using open-source tools and technologies

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

*Note: If you want to quickly run the app with an empty knowledge base (i.e. forget the previously uploaded PDFs), you can run `reset.bat` for Windows or `reset.sh` for Unix-like systems. Alternatively, you can manually delete the contents of the `data` folder and delete the `chroma_db_data` folder entirely.*

# Demo
## Upload your PDF
https://github.com/casie-aviles/botpdf-llama2-chatbot/assets/80239105/3185a3d4-36c9-41e4-8da0-cba8f1dde633
## Ask away
https://github.com/casie-aviles/botpdf-llama2-chatbot/assets/80239105/27717982-ced6-4ba3-921f-64191210a9fd
## Multiple uploads
https://github.com/casie-aviles/botpdf-llama2-chatbot/assets/80239105/94a2f3a8-d296-4a1f-94cc-69d2447f7fa6
## Cross-reference your PDFs
https://github.com/casie-aviles/botpdf-llama2-chatbot/assets/80239105/2c76dba5-a654-43ae-b6c0-31f6621584fa

# Feedback
All manner of feedback is highly appreciated. I am relatively new to this and I would love to hear your comments and suggestions as part of the learning experience. Thank you!



