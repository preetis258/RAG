
class Splitter:
    def __init__(self):
        pass

    def simple_splitter(self, document, chunk_size=2000, chunk_overlap=500):
        chunk_present_start_idx = 0
        chunks = []

        while chunk_present_start_idx < len(document):
            chunk_start_idx = chunk_present_start_idx
            chunk_end_idx = chunk_start_idx + chunk_size
            chunk = document[chunk_start_idx: chunk_end_idx]
            chunks.append(chunk)

            chunk_present_start_idx = chunk_end_idx - chunk_overlap    
        return chunks