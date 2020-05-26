#!/usr/bin/env python3
import logging
import subprocess
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
        
        self.filetypes = {'link':'href','img':'src'}

        #check if the path exists to save files
        if os.path.exists(DEFAULT_DIRPATH):
            # if true change to that working directory
            try:
                os.chdir(DEFAULT_DIRPATH)
                subprocess.check_output(["rm","-rf","*"])
                os.mkdir(DEFAULT_DIRNAME)
                #TODO Check if we are in the right directory
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

    def get_files(self):
        """
        This does the downloading after curating the html and getting
        it as a  soup
        """
        files_to_download = [] #maintaining a list of files to download
        for key,value in self.filetypes.items():
            for k in self.soup.findAll(key):
                files = k.get(value)
                print(files)
                if files is not None and files.startswith("/") or files.startswith("css"):
                    files_to_download.append(files)

        return files_to_download

    def download_js(self):
        """
        Download all the js files that are available on the site
        """
        #TODO Remove the below array
        files = []
        for j in self.soup.findAll("script"):
            js = j.get("src")
            if js is not None and js.startswith("/"):
                files.append(js)
        return js

    def download_img(self):
        """
        Download all the ava[ilable images on thes site
        """
        files = []
        for j in self.soup.findAl("img"):
            img = j.get("src")
            if img is not None:
                files.append(img)
        return files

    def __exit__(self):
        pass

                
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download source files of a website.')
    parser.add_argument("--url",dest="url",action="store",help="this is the url for the website you wish to clone")
    args = parser.parse_args()
    url = args.url
    client = FilesDownloader(url)
    for i in client.get_files():
        print(i)
