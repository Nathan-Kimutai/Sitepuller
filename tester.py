#!/usr/bin/python3.7

import sys
import os
import requests
from bs4 import BeautifulSoup
"""
I wrote this code when I was a python noob
So bear with me if you see some noobish stuff here
"""
html=requests.get(sys.argv[1]).text
the_soup=BeautifulSoup(html,"html.parser")
filetypes={'link':'href','img':'src'}
for key,value in filetypes.items():
    for k in the_soup.findAll(key):
        files=k.get(value)
        if files.startswith("/") or files.startswith('css'):
            print(files)
            url=sys.argv[1]
            #print(files)
            links=url+files
            basename=os.path.basename(files)
            #print(basename)
            #download the files
            resp=requests.get(links).content
            filepipe=open(os.path.basename(links),'wb')
            filepipe.write(resp)
            filepipe.close()
            #do the actual replacement of files
            #print("Replacing {} with {}".format(files,basename))
            offset=len(files)
            #print(offset)
            index=html.find(files)
            #print(html[html.find(files):html.find(files)+len(files)],basename)
            holla=html.replace(html[index:index+offset],basename)
            html=holla

        else:
            pass

for j in the_soup.findAll('script'):
    js=j.get('src')
    if not js ==None and js.startswith("/"):
        basenamejs=os.path.basename(js)

        resp=requests.get(sys.argv[1]+js).content
        filepipe=open(basenamejs,'wb')
        filepipe.write(resp)
        filepipe.close()

        offsetjs=len(js)
        pos=html.find(js)
        print(html[pos:pos+offsetjs])
        hollajs=html.replace(html[pos:pos+offsetjs],basenamejs)
        html=hollajs

fd=open('index.html','w')
fd.write(html)
fd.close()
