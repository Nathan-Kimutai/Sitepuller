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
        ## TODO: I cant be opening and closing a zip_obj each and every time
        ## # TODO: Make sure that I write all the files and then close it after all the files
        ## have been written to the object
        try:
            this.zip_obj.write(filename)
        except Exception as err:
            ## TODO: Add a real logging here and not print the error functionality
            print(err)
        finally:
            this.zip_obj.close()
