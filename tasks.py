# tasks.py

from celery import Celery
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from models.article import insert_article
from utils.llm import generate_article_content
import datetime, uuid

celery_app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery_app.task(bind=True)
def generate_article_task(self, website_id):
    """
    Celery task to generate an article using the LLM and store it in MongoDB.
    """
    content = generate_article_content(prompt=f"Generate an article for website {website_id}")
    article_id = str(uuid.uuid4())
    article_data = {
        "article_id": article_id,
        "website_id": website_id,
        "title": f"Generated Title {article_id[:8]}",
        "content": content,
        "image_url": "https://example.com/default-image.jpg",
        "published_date": datetime.datetime.utcnow(),
        "metadata": {
            "tags": ["sample", "generated"],
            "author": "AI",
            "extra_info": "Additional metadata placeholder."
        }
    }
    insert_article(article_data)
    return article_id
