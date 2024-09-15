# Document Retrieval System

## Overview
This project is a document retrieval system that allows for efficient retrieval of context for chat applications using document vectors and semantic similarity.

## Setup and Running
1. Clone the repository:
    ```
    git clone https://github.com/your-repo/document_retrieval.git
    cd document_retrieval
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run the application:
    ```
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

4. Build and run using Docker:
    ```
    docker build -t document_retrieval .
    docker run -p 8000:8000 document_retrieval
    ```

## API Endpoints
- **/health**: Check if the API is active.
- **/search**: Perform a document search with query parameters:
    - `text`: The search text.
    - `user_id`: Unique identifier for the user.
    - `top_k`: Number of results to return (default: 5).
    - `threshold`: Similarity score threshold (default: 0.5).

## Caching Strategy
We use Redis for caching search results to speed up repeated queries. The cache uses keys based on user ID and query text and expires after 10 minutes.

## Background Task
We use Celery to run background tasks that scrape and index news articles. This process runs independently of the main application thread.

## Rate Limiting
Users are limited to 5 requests per hour. If a user exceeds this limit, they will receive an HTTP 429 status code.

## Future Enhancements
- Implement re-ranking algorithms for more accurate search results.
- Provide fine-tuning scripts for domain-specific retrievers.
