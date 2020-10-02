from zipfile import ZipFile
filepath=""
with ZipFile(filepath,"r") as zip_:
zip_.printdir()
zip_.extractsall()
