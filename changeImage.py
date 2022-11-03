#! /usr/bin/env python3

import os
from PIL import Image


def set_folder(folder):
  # If user input is a valid directory, pass folder to list processor.  Otherwise return "Folder not found" 
  if os.path.isdir(folder):
    list_files(os.path.join(os.getcwd(), folder))
  else:
    print("Folder not found")

def list_files(path):
  # Generate a list of file and folders within the directory from user.  Files are converted to jpg if they are image files.
  # Folders are passed back to same function recursively to scan for more files and folders.
  files = os.listdir(path)
  for file in files:
    if os.path.isdir(os.path.join(path, file)):
      print("Found sub-folder")
      list_files(os.path.join(path, file))
    else:
      try:
        with Image.open(os.path.join(path, file)).convert('RGB') as im:
          new_im = im.resize((600,400))
          new_im.save(os.path.join(path, file.replace(".tiff", "")) + ".jpeg")
      except OSError:
          pass

if __name__ == '__main__':
  set_folder(input("Please enter folder location to be processed: \n(This can be either an absolute path or a relative path)\n"))

