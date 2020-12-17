from mutagen.mp4 import MP4
import os
import re
import subprocess

DIR = 'music/working/CD 413'

matched = []
not_matched = []

for entry in os.scandir(DIR):
    if re.match(r'^\d\d Track \d\d\.m4a$', entry.name) and entry.is_file():
        print(entry.path)
        subprocess.run(['open', entry.path], check=True)

        print('Enter metadata (tab separated):')
        values = input("track, artist, album, year, date_added, genre:\n").split('\t')
        track, artist, album, year, date_added, genre = values

        audio = MP4(entry.path)
        audio.delete()    # delete existing metadata
        audio.tags['\xa9nam'] = track
        audio.tags['\xa9alb'] = album
        audio.tags['\xa9ART'] = artist
        audio.tags['\xa9day'] = year
        audio.tags['purd']    = date_added
        audio.tags['\xa9gen'] = genre
        audio.save()
        os.rename(entry.path, entry.path.replace(entry.name, f'{track}.m4a'))
