from sys import argv
import os

def mkvpropedit_binary():
  path = None
  try:
    i = argv.index("--mkvpropedit-bin-path")
    if i + 1 >= len(argv): return None
    path = argv[i + 1]
  except ValueError:
    return None
  
  if os.path.exists(path):
      return path
  else:
    raise FileNotFoundError(f"mkvpropedit binary not found at {path}")
  
def mediainfo_binary():
  path = None
  try:
    i = argv.index("--mediainfo-bin-path")
    if i + 1 >= len(argv): return None
    path = argv[i + 1]
  except ValueError:
    return None
  
  if os.path.exists(path):
      return path
  else:
    raise FileNotFoundError(f"mediainfo binary not found at {path}")

def input_file():
  path = None
  try:
    i = argv.index("--input-file")
    if i + 1 >= len(argv): return None
    path = argv[i + 1]
  except ValueError:
    return None
  
  if not os.path.exists(path):
    return None
  
  if os.path.isfile(path):
    return path
  else:
    raise ValueError(f"{path} is not a file")
  
def folder_input():
  path = None
  try:
    i = argv.index("--input-folder")
    if i + 1 >= len(argv): return None
    path = argv[i + 1]
  except ValueError:
    return None
  
  if not os.path.exists(path):
    return None
  
  if os.path.isdir(path):
    return path
  else:
    raise ValueError(f"{path} is not a directory")
  

