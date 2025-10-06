class VectorDB:
    def __init__(self):
        self.store = []

    def add(self, embedding, meta):
        self.store.append((embedding, meta))

    def query(self, query_vector, top_k=5):
        return self.store[:top_k]