from sentence_transformers import SentenceTransformer
import numpy as np

# Load the encoder model
encoder_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def perform_vector_search(text, top_k, threshold):
    # Encode the search query into a vector
    query_vector = encoder_model.encode(text)

    # Fetch documents and their vectors from the database (pseudo-code)
    documents = fetch_documents_from_database()  # Replace with actual DB call

    # Perform similarity search
    results = []
    for doc in documents:
        doc_vector = doc['vector']
        similarity = np.dot(query_vector, doc_vector)  # Using dot product for similarity
        if similarity > threshold:
            results.append({"document": doc['content'], "similarity": similarity})
    
    # Sort results by similarity and get top_k
    results = sorted(results, key=lambda x: x['similarity'], reverse=True)[:top_k]
    return results
