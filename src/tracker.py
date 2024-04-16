import os
import json

def get_fs_last_edit(file_path):
  return int(os.path.getmtime(file_path))

loaded = {}
tracker_file_path = "tracker.json"

def load():
  global loaded
  with open(tracker_file_path, "r") as f:
    loaded = json.load(f)

def get_last_edit(file_path):
  return loaded.get(file_path, None)

def set_last_edit(file_path, last_edit):
  loaded[file_path] = last_edit
  with open(tracker_file_path, "w") as f:
    json.dump(loaded, f)

def should_be_processed(file_path):
  last_edit = get_last_edit(file_path)
  if last_edit is None:
    return True
  
  return last_edit != get_fs_last_edit(file_path)