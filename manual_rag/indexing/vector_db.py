import faiss
import numpy as np


class VectorDB:
    def __init__(self):
        self.index = None

    def create_faiss_index(self, embeddings):
        embeddings = np.array(embeddings).astype("float32")

        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(embeddings)

        dimension = embeddings.shape[1]

        # Inner Product on normalized vectors = cosine similarity
        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(embeddings)

        return self.index

    def save_faiss_index(self, index, path):
        faiss.write_index(index, path)

    def load_faiss_index(self, path):
        self.index = faiss.read_index(path)

        return self.index

    def search(self, query_embedding, k=3):
        query_embedding = np.array(query_embedding).astype("float32")

        # Normalize query vector
        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(
            query_embedding,
            k
        )

        return scores, indices