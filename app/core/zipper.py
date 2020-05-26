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

    def __enter__(self):
        for rel,stuff,filaname in os.walk("."): 
            print(filename)

    def write_to_zip(self,filename):
        """
        Write files passed to the method as arguments to the
        zip file object
        """
        try:
            with open(filename,"rb") as f:
                self.zip_obj.write(f.read)
        except Exception as err:
            logging.error(err)

    def close_zip_obj(self):
        """
        Close the zip object
        """
        self.zip_obj.close()
    
    def __exit__(self):
        self.close_zip_obj()

if __name__ == "__main__":
    path = "../downloads/"
    zip_filename = "website.zip"
    zipper = MyZipper(path,zip_filename)
    for _,_,filenames in os.walk(path):
        for files in filenames:
            print(filenames)
            zipper.write_to_zip(files)
