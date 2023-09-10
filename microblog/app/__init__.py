from flask import Flask

app = Flask(
    __name__, template_folder="/home/soft-dev/blog-app-miguel/microblog/templates"
)

from app import routes
