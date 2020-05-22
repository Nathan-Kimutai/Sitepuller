from flask import Blueprint,render_template,redirect,url_for,request
from ..core.downloader import FilesDownloader

main = Blueprint('main',__name__)

@main.route("/",methods=['GET','POST'])
def index():
    """
    url = "https://comma.ai"
    client = FilesDownloader(url)
    data = client.download()
    """
    url = request.form.get("url")
    ## TODO: Check if the url is valid and show the user a valid format to submit urls
    
    return render_template("index.html")
