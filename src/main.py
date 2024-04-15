from os import walk, path

import mkvpropedit
import mediainfo
import args
from media import Media
from title import generate_title

def main():
  if not mediainfo.is_installed():
    print("mediainfo is not installed")
    return

  if not mkvpropedit.is_installed():
    print("mkvpropedit is not installed")
    return
  
  file_path = args.input_file()
  if file_path is not None:
    return process_file(file_path)
  

  folder_path = args.folder_input()
  if folder_path is not None:
    for root, _, filenames in walk(folder_path):
      for filename in filenames:
        file_path = path.join(root, filename)
        process_file(file_path)

def process_file(file_path):
  if not file_path.endswith(".mkv"): return

  info = mediainfo.get_info(file_path)
  media = Media(info)

  new_titles = {}
  
  for track in media.tracks:
    new_titles[track.id] = generate_title(track)

  if mkvpropedit.set_new_titles(file_path, new_titles):
    print(f"Titles updated successfully ({file_path})")
  else:
    print("Failed to update titles")
  
if __name__ == "__main__":
  main()