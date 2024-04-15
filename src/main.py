import mkvpropedit
import mediainfo
import args
from media import Media
from title import generate_title

def main():
  if args.validate_args():
    print("Usage:\npython main.py --input-file <file>\npython main.py --folder-input <folder>")
    return
  
  if not mediainfo.is_installed():
    print("mediainfo is not installed")
    return

  if not mkvpropedit.is_installed():
    print("mkvpropedit is not installed")
    return
  
  path = args.input_file()
  process_media(path)

def process_media(path):
  info = mediainfo.get_info(path)
  media = Media(info)

  new_titles = {}
  
  for track in media.tracks:
    new_titles[track.id] = generate_title(track)

  if mkvpropedit.set_new_titles(path, new_titles):
    print("Titles updated successfully")
  else:
    print("Failed to update titles")
  
if __name__ == "__main__":
  main()