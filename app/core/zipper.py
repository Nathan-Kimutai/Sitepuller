from zipfile import ZipFile
import logging
import os

PATH = "../downloads/website"

class MyZipper:
    """
    MyZipper is what will be used to zip files that are going to be downloaded from the server and add them to the
    zipfile at the downloads files
    """
    def __init__(self,path_name,zip_name):
        self.path = path_name
        self.zip_name = zip_name
        self.zip_obj = ZipFile(self.path + self.zip_name,"w")
    
    #create a zip file with files in it
    def create_zip(self):
        for folderName, subfolders, filenames in os.walk(PATH):
            for filename in filenames:
                #create complete filepath of file in directory
                filePath = os.path.join(folderName, filename)
                self.zip_obj.write(filePath, os.path.basename(filePath))
        print("Success")

if __name__ == "__main__":
    path = "../downloads/"
    zip_filename = "website.zip"
    zipper = MyZipper(path,zip_filename)
    zipper.create_zip()
