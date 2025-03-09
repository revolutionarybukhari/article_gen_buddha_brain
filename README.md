# AI Content API

This project is an AI-driven content generation system that automatically generates articles for websites and serves them via API endpoints. The system uses a central MongoDB database to store articles and website data. React‑based websites can fetch articles dynamically through API requests.

## Project Structure

ai-content-api/ ├── app.py # Main Flask application with API endpoints for website registration and article fetching ├── config.py # Configuration settings (MongoDB URI, server settings, LLM settings, etc.) ├── requirements.txt # Python dependencies ├── tasks.py # Celery task definitions for asynchronous article generation (optional) ├── models/ # Database models for MongoDB interactions │ ├── init.py │ ├── article.py # Functions related to article storage and retrieval │ └── website.py # Functions related to website registration and retrieval ├── utils/ # Utility functions for LLM integration │ └── llm.py ├── logs/ # Log files for the application │ └── app.log ├── tests/ # Test cases for API endpoints │ └── test_api.py └── README.md # Project documentation


## Features

- **Website Registration:**  
  Websites register their domain (and optionally a custom website_id). They can later fetch articles using API requests.
  
- **Article Generation:**  
  Articles are generated automatically using an LLM (using either OpenAI's GPT‑3.5‑turbo or a local Llama model). Each article includes:
  - Title
  - Content
  - Image URL (for article images)
  - Published date
  - Metadata (tags, author, and extra info for future enhancements)

- **API Endpoints:**  
  - `POST /api/webhook/register`: Register a website.
  - `GET /api/articles?website_id=<id>`: Retrieve all articles for a website.
  - `GET /api/article/<article_id>`: Retrieve a specific article by ID.
  - `GET /api/test_generate/<website_id>`: Test endpoint to generate and store an article.

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

Environment Variables:
Configure the following as needed:

MONGODB_URI: MongoDB connection string (default: mongodb://localhost:27017/)
DATABASE_NAME: Database name (default: content_db)
FLASK_HOST: Flask host (default: 0.0.0.0)
FLASK_PORT: Flask port (default: 5000)
CELERY_BROKER_URL: Celery broker URL (default: redis://localhost:6379/0)
CELERY_RESULT_BACKEND: Celery result backend (default: redis://localhost:6379/0)
LLM_TYPE: "openai" (for GPT‑3.5‑turbo) or "llama" (for a local model) (default: openai)
OPENAI_API_KEY: API key for OpenAI (if using GPT‑3.5)
LLAMA_MODEL_NAME: Model name for Llama (if using Llama)

Run the Flask app:
python app.py
Run Celery Worker (optional, for asynchronous tasks):
celery -A tasks.celery_app worker --loglevel=info
Run tests:
python -m unittest discover tests
Integration with React Websites

React-based websites can fetch articles dynamically using API requests. For example, using Axios:

import axios from 'axios';

const fetchArticles = async (websiteId) => {
  try {
    const response = await axios.get(`https://your-api-domain.com/api/articles?website_id=${websiteId}`);
    return response.data.articles;
  } catch (error) {
    console.error("Error fetching articles:", error);
    return [];
  }
};
License

This project is licensed under the MIT License.


---

### 11. logs/app.log

Create an empty file (used for logging):

```bash
# logs/app.log
# (This file is used for logging; leave it empty initially.)
