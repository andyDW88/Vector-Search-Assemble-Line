# Function to embed a query and perform a vector search
def query_and_display(query):
    query_embedding = embeddings.embed_documents([query])[0]
    
    # Retrieve relevant child documents based on query
    child_docs = collection.aggregate([{
        "$vectorSearch": {
            "index": "vector_index",
            "path": "embedding",
            "queryVector": query_embedding,
            "numCandidates": 10
        }
    }])
    
    # Fetch corresponding parent documents for additional context
    parent_docs = [collection.find_one({"_id": doc['parent_ref']}) for doc in child_docs]
