import os
from flask import Blueprint,render_template,redirect,url_for,request,flash,current_app,send_file
from ..core.downloader import FilesDownloader

main = Blueprint('main',__name__)

@main.route("/",methods=['GET','POST'])
def index():
    return render_template("index.html")

@main.route("/download",methods=['GET','POST'])
def download_site():
    uploads = os.path.join(current_app.root_path,"downloads") + "/website.zip"
    return send_file(uploads, as_attachment=True)
