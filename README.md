# MkvStreamTitleNormalizer

Python script that "normalizes" stream titles inside a Matroska file. The generated titles are based on the stream specifications. Under the hood, this tool uses [`mkvpropedit`](https://mkvtoolnix.download/doc/mkvpropedit.html) and [`mediainfo`](https://mediaarea.net/en/MediaInfo).

## Usage

This tool can be used in two ways:

1. One file mode: In this mode you pass a file and the script will normalize the stream titles of that file.

```bash
python src/main.py --input-file /path/to/file.mkv
```

2. Folder mode: In this mode you pass a folder and the script will normalize the stream titles of all the Matroska files inside that folder (recursive).

```bash
python src/main.py --input-folder /path/to/folder
```

### Additional options

If the binaries of `mkvpropedit` amd/or `mediainfo` are not in the path or you want to use a specific binary you can pass the path of the binaries using the `--mkvpropedit-bin-path` and `--mediainfo-bin-path` arguments.

```bash
python src/main.py --input-file /path/to/file.mkv --mkvpropedit-bin-path /path/to/mkvpropedit --mediainfo-bin-path /path/to/mediainfo
```

## Tracker mode

This tool includes a tracker mode. This mode will keep track of which files are processed and which are not. If a file has been processed it will not be processed again. This is useful when you have a large amount of files and you want to process them in batches.

To use the tracker mode you need to pass the `--use-tracker` argument.

> [!NOTE]  
> The program does not use the hash of a file to determine if it has been processed as some files can be extremely large. Instead it uses the last modification time of the file. With that being said, if you modify the file after it has been processed the program will process it again.

## Process speed

Due to the nature of `mkvpropedit`, the process time is very short. `mkvpropedit` modifies the properties of a Matroska file without a complete remux which results in fast processing times.

## Title normalization

The normalization process can be found in the `src/title.py` file.

### Video streams

Format: `{Resolution} {HDR Format}`

Examples:

- `4K Dolby Vision`
- `1080p HDR10`
- `1080p HLG`
- `720p SDR`

### Audio streams

Format: `{Language} {Channels} ({Codec}) ({Dolby Atmos})`

Examples:

- `French 7.1 (DD+) (Dolby Atmos)`
- `English 5.1 (DTS)`
- `Spanish Stereo`
- `English 7.1 (TrueHD) (Dolby Atmos)`
- `English Mono`
