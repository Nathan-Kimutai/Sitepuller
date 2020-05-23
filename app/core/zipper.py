from zipfile import ZipFile
import logging
import os
# zipObj = ZipFile("../website.zip","w")

class MyZipper:
    """
    MyZipper is what will be used to zip files that are going to be downloaded from the server and add them to the
    zipfile at the downloads files
    """
    def __init__(self,path_name,zip_name):
        self.path = path_name
        self.zip_name = zip_name
        self.zip_obj = ZipFile(self.path + self.zip_name,"w")

    def write_to_zip(self,filename):
        """
        Write files passed to the method as arguments to the
        zip file object
        """
        ## TODO: I cant be opening and closing a zip_obj each and every time
        ## # TODO: Make sure that I write all the files and then close it after all the files
        ## have been written to the object
        try:
            fd = open(filename,'r')
            self.zip_obj.write(fd)
        except Exception as err:
            logging.error(err)
        finally:
            # this.zip_obj.close()
            fd.close()

    def close_zip_obj(self):
        """
        Close the zip object
        """
        self.zip_obj.close()

if __name__ == "__main__":
    path = "../downloads/"
    zip_filename = "website.zip"
    zipper = MyZipper(path,zip_filename)
    for _,_,filename in os.walk(path):
        zipper.write_to_zip(filename)
