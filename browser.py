#!/bin/python
# Python Web Browser, Concept
# Build not tied to a release
# experimental-channel
import sys
try:
  import webview
except:
  print("You need to have Pywebview installed to run FreeCat.")
  print("On macOS run:")
  print("pip3 install pywebview")
  print("On Linux run:")
  print("pip install pywebview")
  sys.exit()
import os

engine="pywebview"
enginecmd=""
enginever="3.5"
enginehomepage="https://pywebview.flowrl.com/"
launchargs=""
enginetype="python"
searchengine="built-in"
searchfrombar="unsupported"

webview.create_window('FreeCat', 'src/home.html')
webview.start()
