#!/usr/bin/env python3
import requests
import sys
import os
import re


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
    # Expect to receive back a dictionary variable in the proper format: name, weight, description, image_name
    # The returned dictionary is posted to the url previously entered by user

    #print(file_operation(file))
    response = requests.post(url, json=file_operation(file))


def file_operation(file):
  # Each file is parsed into a dictionary as title, name, date, feedback
  # dictionary is returned to function caller
  fruit = {}
  full_content = open(file, "r")
  fruit["name"] = full_content.readline().strip()
  fruit["weight"] = int(re.findall(r'\d+', full_content.readline().strip())[0])
  description_text = full_content.readlines()

  # Process the last block in the file content.
  # In case there are multiple lines or pure numbers, convert into a single string var
  text = ""
  if type(description_text) == list:
    for line in description_text:
      text = text + str(line).strip()
  else:
    text = str(description_text).strip()

  # Final single string var is stored in the dicionary
  fruit["description"] = text

  # for debugging:
  #print("Title is:\n{}\nSubmitted by {} on {}\nContent:\n{}".format(review["title"], review["name"], review["date"], review["feedback"]))
  full_content.close()

  fruit["image_name"] = os.path.splitext(file)[0] + ".jpeg"

  return fruit



#def posting_online(file):
#  with open(file, 'rb') as opened:
#    r = requests.post(url, files={'file': opened})
#  opened.close()

def main(argv):

  # Ask for user input on posting url and working folder
  # Pass the folder variable into set_folder function for verification
  global url
#  url = input("Enter the URL for posting data:\n")
  url = "http://localhost/fruits/"
  set_folder(input("Please enter folder location to be processed: \n(This can be either an absolute path or a relative path)\n"))
  #set_folder("supplier-data/descriptions")

if __name__ == '__main__':
  main(sys.argv)


