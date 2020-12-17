import csv
from mutagen.mp4 import MP4
import os

DIR = 'music/CD 191'

for entry in os.scandir(DIR):
    if entry.name.endswith(".m4a") and entry.is_file():
        print(entry.path)
    audio = MP4(entry.path)
    print(audio.tags)