#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

import sys
import os
from datetime import date

#def generate_report(filename, title, additional_info, table_data):
def generate_report(filename, title, additional_info):

  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  #report_info = Paragraph(additional_info, styles["BodyText"])
  #table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
  #              ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
  #              ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  #report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  #empty_line = Spacer(1,20)
#  report.build([report_title, empty_line, report_info, empty_line, report_table])
#  report.build([report_title, additional_info])
  build_content = []
  build_content.append(report_title)
  build_content.extend(additional_info)
  #print(build_content)
  report.build(build_content)

def set_folder(folder):
  # If folder is found, start iteration function, if not, alert user.
  if os.path.isdir(folder):
    return iterate_files(os.path.join(os.getcwd(), folder))
  else:
    print("Folder not found")


def iterate_files(path):
  # Set current working folder
  # Scan current working folder for a list of files to be worked on
  os.chdir(path)
  files = os.listdir(os.getcwd())
  print("working in:\n{}\nWill iterate through the following list of files\n{}".format(os.getcwd(),files))

  # Each file in the working folder is passed to operation function to be processed
  empty_line = Spacer(1,20)
  pdf_content = []

  style = getSampleStyleSheet()

  for file in files:
    content = file_operation(file)
    pdf_content.append(Paragraph("name: " + content["name"], style["BodyText"]))
    pdf_content.append(Paragraph("weight: " + content["weight"], style["BodyText"]))
    pdf_content.append(empty_line)

  return pdf_content


def file_operation(file):
  # Each file is parsed into a dictionary as title, name, date, feedback
  # dictionary is returned to function caller
  fruit = {}
  full_content = open(file, "r")
  fruit["name"] = full_content.readline().strip()
  fruit["weight"] = full_content.readline().strip()
  full_content.close()

  return fruit


def main(argv):

  today = date.today()
  # Ask for user input on posting url and working folder
  # Pass the folder variable into set_folder function for verification
  global url
#  url = input("Enter the URL for posting data:\n")
  url = "http://localhost/fruits/"
  #set_folder(input("Please enter folder location to be processed: \n(This can be either an absolute path or a relative path)\n"))
  pdf_content = set_folder("supplier-data/descriptions")
  generate_report("/tmp/processed.pdf", "Processed Update on " + today.strftime("%B %d, %Y"), pdf_content)



if __name__ == '__main__':
  main(sys.argv)

