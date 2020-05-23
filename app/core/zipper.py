from zipfile import ZipFile
# zipObj = ZipFile("../website.zip","w")

class MyZipper:
    """
    MyZipper is what will be used to zip files that are going to be downloaded from the server and add them to the
    zipfile at the downloads files
    """
    def __init__(self,path,zip_name):
        this.path = path
        this.zip_name = zip_name
        this.zip_obj = ZipFile(this.path + this.zip_name,"w")

    def write_to_zip(self,filename):
        """
        Write files passed to the method as arguments to the
        zip file object
        """
        this.zip_obj.write(filename)
