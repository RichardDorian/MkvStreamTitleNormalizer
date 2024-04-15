class Media:
  def __init__(self, data):
    self.tracks = []

    for track in data["media"]["track"]:
      if track["@type"] == "Video":
        self.tracks.append(VideoTrack(track))
      if track["@type"] == "Audio":
        self.tracks.append(AudioTrack(track))

class VideoTrack:
  def __init__(self, data):
    self.id = int(data["ID"])
    self.width = int(data["Width"])
    self.height = int(data["Height"])
    self.hdr_format = data.get("HDR_Format", None)
    self.hdr_format_compat = data.get("HDR_Format_Compatibility", None)
    self.transfer_characteristics = data.get("transfer_characteristics", None)

class AudioTrack:
  def __init__(self, data):
    self.id = int(data["ID"])
    self.language = data.get("Language", None)
    self.channels = int(data["Channels"])
    self.commercial_format = data.get("Format_Commercial_IfAny", None)