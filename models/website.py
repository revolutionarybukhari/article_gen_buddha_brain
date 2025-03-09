# models/website.py

from pymongo import MongoClient
from config import MONGODB_URI, DATABASE_NAME

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
websites_collection = db["websites"]

def register_website(website_data):
    """
    Insert a new website record.
    website_data should be a dictionary containing website_id, domain, and created_at.
    """
    return websites_collection.insert_one(website_data)

def get_website_by_id(website_id):
    """Retrieve website details by website_id."""
    return websites_collection.find_one({"website_id": website_id}, {"_id": 0})
