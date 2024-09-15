from fastapi import FastAPI, HTTPException
import redis
import time
from .search import perform_vector_search

app = FastAPI()
cache = redis.Redis(host='localhost', port=6379, db=0)

@app.get("/health")
def health_check():
    return {"status": "API is active"}

@app.get("/search")
def search(text: str, user_id: str, top_k: int = 5, threshold: float = 0.5):
    # Check user request limit
    user_key = f"user:{user_id}:requests"
    request_count = cache.get(user_key)
    if request_count and int(request_count) > 5:
        raise HTTPException(status_code=429, detail="Request limit exceeded")

    # Increment user request count
    cache.incr(user_key)
    cache.expire(user_key, 3600)  # Optional: Set expiration for rate limit

    # Cache lookup
    cache_key = f"{user_id}:{text}"
    cached_result = cache.get(cache_key)
    if cached_result:
        return cached_result

    # Perform vector search
    start_time = time.time()
    results = perform_vector_search(text, top_k, threshold)
    inference_time = time.time() - start_time

    # Log inference time
    print(f"Inference time: {inference_time:.2f}s")

    # Cache the results
    cache.set(cache_key, results, ex=600)  # Cache for 10 minutes
    return results
