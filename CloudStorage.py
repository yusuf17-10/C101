import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)


def main():
    access_token="sl.Asp4K-jOHmnhZoy4DBpK5JXeKsoax7lZH8T8h8Qi-s3QrsJqRL6XfX6vYB5-b5c7T81rsd7ecuOelNaFj-kvH8CehN-2sfTu7GuLHC6ZEeo2kipC7ni2d35o7Ka0FaE7bETgKTk"
    transferdata=TransferData(access_token)
    file_from=input("Enter The File path to transfer :  ")
    file_to=input("Enter the full path to uplaod to dropbox :  ")
    transferdata.upload_file(file_from,file_to)


if __name__ == "__main__":
    main()
