from os import getenv
import subprocess

import args

def binary_path():
  env = args.mkvpropedit_binary()
  if env is not None:
    return env
  
  env = getenv("MKVPROPEDIT_BIN")
  if env is not None:
    return env
  
  return "mkvpropedit"

def is_installed():
  process = subprocess.run([binary_path(), "--version"], stdout=subprocess.DEVNULL)
  return process.returncode == 0

def set_new_titles(file, titles):
  args = []

  for id, title in titles.items():
    args.extend(["--edit", f"track:{id}", f"--set", f"name={title}"])

  return run(file, args)

def run(file, args = []):
  process = subprocess.run([binary_path(), file, *args], stdout=subprocess.DEVNULL)
  return process.returncode == 0