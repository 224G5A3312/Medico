from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_hugging_face_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec 
from langchain_pinecone import PineconeVectorStore
from langchain_community.vectorstores import DocArrayInMemorySearch

load_dotenv()


PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')

# Only set env vars if values are present to avoid assigning None (TypeError)
if PINECONE_API_KEY:
    os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
if GOOGLE_API_KEY:
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


extracted_data=load_pdf_file(data='data/')
filter_data = filter_to_minimal_docs(extracted_data)
text_chunks=text_split(filter_data)

embeddings = download_hugging_face_embeddings()

index_name = "medical-chatbot"

if PINECONE_API_KEY:
    pinecone_api_key = PINECONE_API_KEY
    pc = Pinecone(api_key=pinecone_api_key)
    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
    _ = pc.Index(index_name)
    _ = PineconeVectorStore.from_documents(
        documents=text_chunks,
        index_name=index_name,
        embedding=embeddings,
    )
else:
    _ = DocArrayInMemorySearch.from_documents(text_chunks, embeddings)