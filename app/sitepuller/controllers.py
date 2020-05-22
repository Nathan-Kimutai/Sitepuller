from flask import Blueprint,render_template,redirect,url_for
from ..core.downloader import FilesDownloader

main = Blueprint('main',__name__)

@main.route("/")
def index():
    url = "https://comma.ai"
    client = FilesDownloader(url)
    data = client.download()
    return render_template("index.html",data=data)
