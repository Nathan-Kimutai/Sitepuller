#!/usr/bin/env python3
import logging
import subprocess
import re
import sys
import os
import requests
import argparse
from bs4 import BeautifulSoup

base_dir = os.path.abspath(os.path.dirname(__file__)) + "/../downloads"

DEFAULT_DIRNAME =  "website"
DEFAULT_DIRPATH =  base_dir

class FilesDownloader:
    """
    This is the main functionality of Sitepuller,
    and this is the class that dowloads the files
    """
    #TODO Improve this file every day to make it download almost anything and anysite
    def __init__(self,url):
        if url:
            self.url = url
        else:
            logging.warning("The url cannot be empty")
            sys.exit(1)

        try:
            self.raw_html= requests.get(self.url)
        except:
            logging.error("We could not find the page please check your internet connection and try again")
            sys.exit(1)
        self.text_html = self.raw_html.text
        self.soup = BeautifulSoup(self.text_html,"html.parser")
        #this are all the tags and and their attributes to look at while
        # downloading all the content from a page

        self.filetypes = {'link':'href','img':'src','script':'src'}

        #check if the path exists to save files
        if os.path.exists(DEFAULT_DIRPATH):
            # if true change to that working directory
            try:
                os.chdir(DEFAULT_DIRPATH)
                os.mkdir(DEFAULT_DIRNAME)
            except Exception as e:
                #handle the exception and log out the errors
                logging.error(e)
                #if the path does not exitst create it
        else:
            self.create_directory()
    def create_directory(self):
        """
        Create the directory to save the files to be downloaded
        """
        try:
            os.mkdir(DEFAULT_DIRPATH)
        except Exception as e:
            logging.error(e)

    def find_internal_links(self):
        #find all the internal links and build the map of the website
        pass

    def files_to_download(self):
        files_to_download = []
        for key,value in self.filetypes.items():
            for k in self.soup.findAll(key):
                files = k.get(value)
                if files is not None and files.startswith("/") or files is not None and files.startswith("css"):
                    files_to_download.append(self.url + files)
        return files_to_download

    def download_js(self):
        js_files = [x for x in self.files_to_download() if x.endswith(".js")]
        #print(os.getcwd())
        self.cd_website()
        try:
            os.mkdir("js")
        except Exception as e:
            pass
        for f in js_files:
            basename = os.path.basename(f)
            resp = requests.get(f).content
            file_path = os.path.join(os.getcwd() + "/js/",basename)
            print(file_path)
            with open(file_path,'wb') as fd:
                fd.write(resp)
                print("Writing {} to {}".format(basename,file_path),flush=True)
        #return something to show that there was a success
        return "Success"

    def download_img(self):
        img_files = [x for x in self.files_to_download() if x.endswith(".png") or x.endswith(".jpg") or x.endswith(".jpeg") or \
            x.endswith(".ico")]
        #change to the the website directory
        self.cd_website()
        try:
            os.mkdir("img")
        except Exception as e:
            print("The directory already exists or cannot be created")
            pass 
        except Exception as e:
            pass 
        #download and save the images to img folder
        for img in img_files:
            basename = os.path.basename(img)
            file_path = os.path.join(os.getcwd() + "/img/",basename)
            resp = requests.get(img).content 
            print(file_path)
            with open(file_path,"wb") as fd:
                fd.write(resp)
                print("Writing {} to {}".format(basename,file_path),flush=True)

    #TODO search for all the css files burried deep in the links in the page
    def search_css(self):
        pass

    def cd_website(self):
        try:
            os.chdir("website")
        except Exception as e:
            print("Already in the directory")

    def __exit__(self):
        pass

#added this part for testing purposes otherwise this all program won't run here
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download source files of a website.')
    parser.add_argument("--url",dest="url",action="store",help="this is the url for the website you wish to clone")
    args = parser.parse_args()
    url = args.url
    client = FilesDownloader(url)
    client.download_img()
    client.download_js()
