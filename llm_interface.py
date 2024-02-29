import time
import chromadb

from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex, ServiceContext, StorageContext, SimpleDirectoryReader

llm = Ollama(model='llama2')
print(llm.metadata)

def stream_response(prompt):
    """
    Streams the completion of a prompt using a large language model (LLM).

    Args:
    - prompt (str): The prompt text to be completed by the language model.

    Returns:
    - delta (float): The delta value associated with each response generated
      by the language model in response to the provided prompt.

    Notes:
    - This function streams the completion of a given prompt using a language
      model (LLM) and yields the delta values associated with each response
      generated by the model.
    - The delta value represents a measure of difference or change associated
      with each response.
    - A small delay of 0.02 seconds is introduced between each iteration to
      control the streaming rate.

    Example:
    >>> for delta in stream_response("Generate a summary for a given text"):
    >>>     print(delta)
    """
    start_time = time.time()

    response = llm.stream_complete(prompt)
    for token in response:
        yield token.delta

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("stream_response() elapsed time:", elapsed_time, "seconds")

def search_pdf(query):
    """
    Function to search for a given query in a collection of PDF documents 
    and return the response generator.
    
    Args: 
    - query (str): The query string to search for in the PDF documents.
    
    Returns:
    - response (str): A response generator containing the search results.
    """
    start_time = time.time()
    documents = SimpleDirectoryReader("data/").load_data()

    # Create Chroma DB client and store
    client = chromadb.PersistentClient(path="./chroma_db_data")
    chroma_collection = client.get_or_create_collection(name="reviews")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Initialize ServiceContext
    service_context = ServiceContext.from_defaults(llm=llm, embed_model="local")

    # Create VectorStoreIndex and query engine
    index = VectorStoreIndex.from_documents(documents,
                                            service_context=service_context,
                                            storage_context=storage_context)
    query_engine = index.as_query_engine(streaming=True)

    # Query
    response = query_engine.query(query)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("search_pdf() elapsed time:", elapsed_time, "seconds")

    return response.response_gen
