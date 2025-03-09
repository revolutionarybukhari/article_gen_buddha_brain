# app.py

from flask import Flask, request, jsonify
import datetime, uuid
from models.website import register_website, get_website_by_id
from models.article import get_articles_by_website, get_article_by_id, insert_article
from utils.llm import generate_article_content
from config import FLASK_HOST, FLASK_PORT

app = Flask(__name__)

@app.route('/api/webhook/register', methods=['POST'])
def register_website_endpoint():
    """
    Registers a website.
    Expected JSON payload:
    {
      "website_id": "optional-custom-id",
      "domain": "example.com"
    }
    """
    data = request.json
    if not data or "domain" not in data:
        return jsonify({"error": "Missing required field: domain"}), 400

    website_data = {
        "website_id": data.get("website_id", str(uuid.uuid4())),
        "domain": data["domain"],
        "created_at": datetime.datetime.utcnow()
    }
    register_website(website_data)
    return jsonify({"status": "registered", "website_id": website_data["website_id"]})

@app.route('/api/articles', methods=['GET'])
def fetch_articles():
    """
    Fetch all articles for a given website.
    Expects query parameter: website_id
    """
    website_id = request.args.get("website_id")
    if not website_id:
        return jsonify({"error": "website_id is required"}), 400
    articles = get_articles_by_website(website_id)
    return jsonify({"website_id": website_id, "articles": articles})

@app.route('/api/article/<article_id>', methods=['GET'])
def fetch_article(article_id):
    """
    Fetch a specific article by its article_id.
    """
    article = get_article_by_id(article_id)
    if not article:
        return jsonify({"error": "Article not found"}), 404
    return jsonify(article)

@app.route('/api/test_generate/<website_id>', methods=['GET'])
def test_generate(website_id):
    """
    Test endpoint to generate an article synchronously.
    """
    content = generate_article_content(prompt=f"Generate an article for website {website_id}")
    article_id = str(uuid.uuid4())
    article_data = {
        "article_id": article_id,
        "website_id": website_id,
        "title": f"Test Generated Title {article_id[:8]}",
        "content": content,
        "image_url": "https://example.com/default-image.jpg",  # default image URL
        "published_date": datetime.datetime.utcnow(),
        "metadata": {
            "tags": ["test", "generated"],
            "author": "AI",
            "extra_info": "Additional metadata can be added here."
        }
    }
    insert_article(article_data)
    return jsonify({"status": "Article generated and stored", "article_id": article_id})

if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT)
