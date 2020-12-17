import csv
import os
from plexapi.server import PlexServer

plexurl = ''
token = ''
plex = PlexServer(plexurl, token)
music = plex.library.section('Music')

def track_search(track, artist, album):
    matches = 0
    for this_artist in music.searchArtists(title=artist):
        for this_album in this_artist.albums(title=album):
            for this_track in this_album.tracks(title=track):
                print(this_track)
                print(this_track.title, "\t", this_track.artist().title, "\t", this_track.album().title )
                matches += 1
    return matches

i = 0
with open('purchased2009.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        track = row[0]
        artist = row[1]
        album = row[2]
        year = row[3]
        print(track_search(track, artist, album))
        i += 1
        if i > 10:
            exit()
