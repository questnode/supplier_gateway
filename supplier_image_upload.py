#!/usr/bin/env python3
import requests
import sys
import os

# This example shows how a file can be uploaded using
# The Python Requests module

global url

def set_folder(folder):
  # If folder is found, start iteration function, if not, alert user.
  if os.path.isdir(folder):
    iterate_files(os.path.join(os.getcwd(), folder))
  else:
    print("Folder not found")


def iterate_files(path):
  # Set current working folder
  # Scan current working folder for a list of files to be worked on
  os.chdir(path)
  files = os.listdir(os.getcwd())
  print("working in:\n{}\nWill iterate through the following list of files\n{}".format(os.getcwd(),files))

  # Each file in the working folder is passed to operation function to be processed
  for file in files:
    # Expect to receive back a dictionary variable in the proper format: title, name, date, feedback
    # The returned dictionary is posted to the url previously entered by user

    # filename = os.path.splitext(file)[1]
    if os.path.splitext(file)[1] == ".jpeg":
      posting_online(file)

    #if os.path.splitext(file) = "jpeg"
    #response = requests.post(url, data=file_operation(file))


def posting_online(file):
  with open(file, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
  opened.close()

def main(argv):

  # Ask for user input on posting url and working folder
  # Pass the folder variable into set_folder function for verification
  global url
#  url = input("Enter the URL for posting data:\n")
  url = "http://localhost/upload/"
  set_folder(input("Please enter folder location to be processed: \n(This can be either an absolute path or a relative path)\n"))


if __name__ == '__main__':
  main(sys.argv)


