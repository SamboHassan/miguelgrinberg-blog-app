from flask import Flask
from config import Config

app = Flask(
    __name__, template_folder="/home/soft-dev/blog-app-miguel/microblog/templates"
)
app.config.from_object(Config)

from app import routes
