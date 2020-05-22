#!/usr/bin/python3.7
import sys
import os
import requests
import argparse
try:
    from bs4 import BeautifulSoup
except ImportError:
    raise ImportError("You should first install BeautifulSoup")

FILE_TYPES_TO_DOWNLOAD = {
    "img",
    "js"
}

class FilesDownloader:
    """
    This is the main functionality of Sitepuller,
    and this is the class that dowloads the files
    """
    #TODO Improve this file every day to make it download almost anything and anysite
    def __init__(self,url):
        self.url = url
        self.raw_html= requests.get(self.url)
        self.text_html = self.raw_html.text
        self.soup = BeautifulSoup(self.text_html,"html.parser")
        self.filetypes = {'link':'href','img':'src'}

    def get_files(self):
        """
        This does the downloading after curating the html and getting
        it as a  soup
        """
        files_to_download = []
        for key,value in self.filetypes.items():
            for k in self.soup.findAll(key):
                files = k.get(value)
                if files.startswith("/") or files.startswith("css"):
                    files_to_download.append(files)

        return files_to_download

    def download_js(self):
        """
        Download all the js files that are available on the site
        """

    def download_img(self):
        """
        Download all the available images on thes site
        """

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download source files of a website.')
    parser.add_argument("--url",dest="url",action="store",help="this is the url for the website you wish to clone")
    args = parser.parse_args()
    url = args.url
    client = FilesDownloader(url)
    for i in client.download():
        print(i)
#
# html=requests.get(sys.argv[1]).text
# the_soup=BeautifulSoup(html,"html.parser")
# filetypes={'link':'href','img':'src'}
# for key,value in filetypes.items():
#     for k in the_soup.findAll(key):
#         files=k.get(value)
#         if files.startswith("/") or files.startswith('css'):
#             print(files)
#             url=sys.argv[1]
#             #print(files)
#             links=url+files
#             basename=os.path.basename(files)
#             #print(basename)
#             #download the files
#             resp=requests.get(links).content
#             filepipe=open(os.path.basename(links),'wb')
#             filepipe.write(resp)
#             filepipe.close()
#             #do the actual replacement of files
#             #print("Replacing {} with {}".format(files,basename))
#             offset=len(files)
#             #print(offset)
#             index=html.find(files)
#             #print(html[html.find(files):html.find(files)+len(files)],basename)
#             holla=html.replace(html[index:index+offset],basename)
#             html=holla
#
#         else:
#             pass
#
# for j in the_soup.findAll('script'):
#     js=j.get('src')
#     if not js ==None and js.startswith("/"):
#         basenamejs=os.path.basename(js)
#
#         resp=requests.get(sys.argv[1]+js).content
#         filepipe=open(basenamejs,'wb')
#         filepipe.write(resp)
#         filepipe.close()
#
#         offsetjs=len(js)
#         pos=html.find(js)
#         print(html[pos:pos+offsetjs])
#         hollajs=html.replace(html[pos:pos+offsetjs],basenamejs)
#         html=hollajs
#
# fd=open('index.html','w')
# fd.write(html)
# fd.close()
