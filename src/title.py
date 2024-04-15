from media import VideoTrack, AudioTrack

def generate_title(track: VideoTrack | AudioTrack):
  elements = []
  if isinstance(track, VideoTrack):
    elements.extend([get_video_resolution(track), get_hdr_format(track)])
  
  if isinstance(track, AudioTrack):
    elements.extend([get_language(track), get_audio_channels(track), get_audio_codec(track), get_dolby_atmos(track)])
  
  elements = list(filter(lambda x: len(x) > 0, elements))

  return " ".join(elements)

def get_video_resolution(track: VideoTrack):
  if track.width == 7680: return "8K"
  if track.width == 3840: return "4K"
  if track.width == 1920: return "1080p"
  if track.width == 1280: return "720p"
  if track.width == 720: return "480p"
  if track.width == 640: return "360p"
  if track.width == 426: return "240p"
  if track.width == 320: return "144p"
  return f"{track.height}p"

def get_hdr_format(track: VideoTrack):
  if track.hdr_format is not None:
    if "Dolby Vision" in track.hdr_format: return "Dolby Vision"
    if "HDR10+" in track.hdr_format: return "HDR10"

  if track.hdr_format_compat is not None:
    if "HDR10" in track.hdr_format_compat: return "HDR10"

  if track.transfer_characteristics is not None:
    if "HLG" in track.transfer_characteristics: return "HLG"

  return "SDR"

known_languages = {
  "fr": "French",
  "en": "English",
  "es": "Spanish",
  "de": "German",
  "it": "Italian",
  "pt": "Portuguese",
  "ru": "Russian",
  "ja": "Japanese",
  "ko": "Korean",
  "zh": "Chinese",
  "ar": "Arabic",
  "hi": "Hindi",
  "tr": "Turkish",
  "th": "Thai",
  "nl": "Dutch",
  "sv": "Swedish",
  "fi": "Finnish",
  "da": "Danish",
  "no": "Norwegian",
  "pl": "Polish",
  "cs": "Czech",
  "hu": "Hungarian",
  "el": "Greek",
  "he": "Hebrew",
  "id": "Indonesian",
  "vi": "Vietnamese",
  "ro": "Romanian",
  "fa": "Persian",
  "bg": "Bulgarian",
  "uk": "Ukrainian",
  "sr": "Serbian",
  "hr": "Croatian",
  "sl": "Slovenian",
  "sk": "Slovak",
  "lt": "Lithuanian",
  "lv": "Latvian",
  "et": "Estonian",
  "is": "Icelandic",
  "ga": "Irish",
  "eu": "Basque",
  "ca": "Catalan",
  "gl": "Galician",
  "cy": "Welsh",
  "ab": "Abkhazian",
  "aa": "Afar",
  "af": "Afrikaans",
  "ak": "Akan",
  "sq": "Albanian",
  "am": "Amharic",
  "an": "Aragonese",
  "hy": "Armenian"
}

def get_language(track: AudioTrack):
  if track.language is None: return ''

  # https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes
  if ("qaa" >= track.language and track.language <= "qtz") or track.language == "und" or track.language == "zxx":
    return ""

  language = track.language.lower()
  if language in known_languages:
    return known_languages[language]
  return language

def get_audio_channels(track: AudioTrack):
  if track.channels == 1: return "Mono"
  if track.channels == 2: return "Stereo"
  if track.channels == 6: return "5.1"
  if track.channels == 8: return "7.1"
  return f"{track.channels}.0"

def get_audio_codec(track: AudioTrack):
  codec = ""

  if track.commercial_format is not None:
    if "Dolby TrueHD" in track.commercial_format: codec = "TrueHD"
    if "Dolby Digital" in track.commercial_format: codec = "DD"
    if "Dolby Digital Plus" in track.commercial_format: codec = "DD+"
    if "DTS-HD" in track.commercial_format: codec = "DTS-HD"
    if "DTS" in track.commercial_format: codec = "DTS"

  if len(codec) > 0: return f"({codec})"
  return ""

def get_dolby_atmos(track: AudioTrack):
  if track.commercial_format is not None and "Dolby Atmos" in track.commercial_format:
    return "(Dolby Atmos)"
  return ""
