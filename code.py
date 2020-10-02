from zipfile import ZipFile
file_path="zipfile.zip"
with ZipFile(file_path,"r") as zip_:
  #print the zip content
zip_.printdir()
#extract the content
zip_.extractsall()
