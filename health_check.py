#! /usr/bin/env python3

import sys
import psutil
import email.message
import mimetypes
import os.path
import smtplib
import sys
import shutil
import socket

def generate(sender, recipient, subject, body):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  return message

def send(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()


def main(argv):
  sender = "automation@example.com"
  recipient = "{}@example.com".format(os.environ.get('USER'))
  body = "Please check your system and resolve the issue as soon as possible."

  if psutil.cpu_percent(1) > 80.0:
    subject = "Error - CPU usage is over 80%"
    message = generate(sender, recipient, subject, body)
    send(message)

  d_stat = shutil.disk_usage("/")
  d_free = d_stat.free / d_stat.total
  if d_free < 0.2:
    subject = "Error - Available disk space is less than 20%"
    message = generate(sender, recipient, subject, body)
    send(message)

  free_mem = psutil.virtual_memory().available / (1024.0 ** 2)
  if free_mem < 500:
    subject = "Error - Available memory is less than 500MB"
    message = generate(sender, recipient, subject, body)
    send(message)

  try:
    ip = socket.gethostbyname('localhost')
  except socket.gaierror:
    ip = "failed"

  if ip != "127.0.0.1":
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = generate(sender, recipient, subject, body)
    send(message)


if __name__ == "__main__":
  main(sys.argv)
