from sentence_transformers import SentenceTransformer

class Embeddings:
    def __init__(self):
        pass

    def create_embeddings(self, chunks, model):
        embeddings = model.encode(chunks)
        return embeddings