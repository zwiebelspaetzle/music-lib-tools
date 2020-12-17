import csv
from mutagen.mp4 import MP4
import os
import re
import subprocess
import sys

DIR = sys.argv[1]
TAG_NAMES = ['track', 'artist', 'album', 'year', 'date_added', 'genre']
TRACKS_FILE = 'purchased2009.csv'

tracklist = {}
matched = []
not_matched = []

def safe_filename(new_name: str):
    return new_name.replace('/','_').replace(':','_')

def tag_metadata(audio, metadata):
        audio.delete()    # delete existing metadata
        audio.tags['\xa9nam'] = metadata['track']
        audio.tags['\xa9alb'] = metadata['album']
        audio.tags['\xa9ART'] = metadata['artist']
        audio.tags['\xa9day'] = metadata['year']
        audio.tags['purd']    = metadata['date_added']
        audio.tags['\xa9gen'] = metadata['genre']
        audio.save()
        print('saved')

# import track names, etc., from csv
with open(TRACKS_FILE, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # cd, note, match1, track, artist, album, year, date_added, genre = row
        tracklist[row[0]] = dict(zip(TAG_NAMES, row))

for entry in os.scandir(DIR):
    tagged = False
    print()

    # be choosy about files
    if entry.name.endswith(".m4a") and entry.is_file():
        print(entry.path)
    else:
        continue

    # extract title from metadata
    audio = MP4(entry.path)
    try:
        found_name = audio.tags['\xa9nam'][0]
    except:
        found_name = None
    print(found_name)

    # does this title match something in our tracklist?
    if found_name in tracklist:
        print(tracklist[found_name])
        # tag with data from tracklist
        tag_metadata(audio, tracklist[found_name])
    else:
        # open track for listening
        subprocess.run(['open', entry.path], check=True)
        # prompt for input, and split received string into list
        print('Enter metadata (tab separated):')
        values = input("track, artist, album, year, date_added, genre:\n").split('\t')
        metadata = dict(zip(TAG_NAMES, values))
        tag_metadata(audio, metadata)

    os.rename(entry.path, entry.path.replace(entry.name, f'{safe_filename(found_name)}.m4a'))



# print("\n\n")
# print(f'matched {len(matched)}:')
# print(*matched, sep = "\n")
# print()
# print(f'not matched {len(not_matched)}:')
# print(*not_matched, sep = "\n")