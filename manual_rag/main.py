from manual_rag.indexing.loader import Loader
from manual_rag.indexing.chunking import Splitter
from manual_rag.indexing.embedding import Embeddings
from sentence_transformers import SentenceTransformer
from manual_rag.indexing.vector_db import VectorDB
from manual_rag.retrieval.retriever import Retriever
from manual_rag.retrieval.prompt import Prompt
from manual_rag.retrieval.generator import Generator
import os

loader = Loader()
document = loader.pdf_loader('/home/preeti/Preeti/AI/RAG/data/NovaTech_HR_Policy_Documents.pdf')

splitter = Splitter()
chunks = splitter.simple_splitter(document, 1000,200)
vectordb = VectorDB()

model = SentenceTransformer('all-MiniLM-L6-v2')

if not os.path.exists("faiss_index.bin"):
    
    emb = Embeddings()
    
    embeds = emb.create_embeddings(chunks, model)
    index = vectordb.create_faiss_index(embeds)
    vectordb.save_faiss_index(index, 'faiss_index.bin')
else:
    index = vectordb.load_faiss_index('faiss_index.bin')

query = "How many days of annual leave can a full-time employee carry forward to the following year?"

retriver_obj = Retriever(vectordb, chunks, model)
matches = retriver_obj.retrieve(query, 3)

prompt_obj = Prompt()
final_prompt = prompt_obj.create_prompt(query, matches)

generator_obj = Generator()
response = generator_obj.generate(final_prompt)

print(response)

