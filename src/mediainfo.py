from os import getenv
import subprocess
import json

import args

def binary_path():
  env = args.mediainfo_binary()
  if env is not None:
    return env
  
  env = getenv("MEDIAINFO_BIN")
  if env is not None:
    return env
  
  return "mediainfo"

def is_installed():
  process = subprocess.run([binary_path(), "--version"], stdout=subprocess.DEVNULL)
  return process.returncode == 0

def get_info(file: str):
  process = subprocess.run([binary_path(), "--Output=JSON", file], capture_output=True)
  if process.returncode != 0:
    print("Error getting media info")
    return
  
  data = json.loads(process.stdout)
  return data
  