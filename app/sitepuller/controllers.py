import os
from flask import Blueprint,render_template,redirect,url_for,request,flash,current_app,send_file
from ..core.downloader import FilesDownloader

main = Blueprint('main',__name__)

@main.route("/",methods=['GET','POST'])
def index():
    """
    This is the home route
    """
    if request.method == "POST":
        if request.form.get("url"):
            url = request.form.get("url")
            return redirect(url_for("main.preview"))
        flash("Enter a url")
        ## TODO: Check if the url is valid and show the user a valid format to submit url
    return render_template("index.html")

@main.route("/preview/<url>",methods=['GET','POST'])
def preview(url):
    client = FilesDownloader(url)
    data = client.get_files()
    return render_template("preview.html",data=data)

@main.route("/download",methods=['GET','POST'])
def download_site():
    uploads = os.path.join(current_app.root_path,"downloads") + "/website.zip"
    return send_file(uploads, as_attachment=True)
