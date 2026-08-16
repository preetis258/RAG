class Retriever:
    def __init__(self, vector_db, chunks, embedding_model):
        self.vector_db = vector_db
        self.chunks = chunks
        self.embedding_model = embedding_model

    def retrieve(self, query, k=3):

        # Create query embedding
        query_embedding = self.embedding_model.encode([query])

        # Search FAISS
        scores, indices = self.vector_db.search(
            query_embedding,
            k
        )

        # Map FAISS indices back to actual chunks
        results = []

        for score, index in zip(scores[0], indices[0]):
            results.append({
                "chunk": self.chunks[index],
                "score": float(score),
                "index": int(index)
            })

        return results