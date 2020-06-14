import os
from flask import Blueprint,render_template,redirect,url_for,request,flash,current_app,send_file
from ..core.downloader import FilesDownloader
from ..core.zipper import MyZipper

main = Blueprint('main',__name__)

@main.route("/",methods=['GET','POST'])
def index():
    zip_filename = "website.zip"
    zip_folder = os.path.join(current_app.root_path,"downloads") + "/website/"
    if request.method == "POST":
        url = request.form.get("url")
        client = FilesDownloader(url)
        client.download_js()
        client.download_img()
        zipper = MyZipper(zip_folder,zip_filename)
        zipper.create_zip()
        return redirect(url_for('main.download_site'))
    return render_template("index.html")

@main.route("/android",methods=['GET','POST'])
def android_development():
    return render_template("android.html")

@main.route("/download",methods=['GET','POST'])
def download_site():
    uploads = os.path.join(current_app.root_path,"downloads") + "/website.zip"
    return send_file(uploads, as_attachment=True)
