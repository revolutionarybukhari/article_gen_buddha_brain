# models/article.py

from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
articles_collection = db["articles"]

def insert_article(article_data):
    """Insert a new article document into the collection."""
    return articles_collection.insert_one(article_data)

def get_articles_by_website(website_id):
    """Retrieve all articles for a specific website."""
    return list(articles_collection.find({"website_id": website_id}, {"_id": 0}))

def get_article_by_id(article_id):
    """Retrieve a single article by its article_id."""
    return articles_collection.find_one({"article_id": article_id}, {"_id": 0})
