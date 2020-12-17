import os
from itunesLibrary import library

path = 'z-Library.xml'

lib = library.parse(path)

print("total items:")
print(len(lib))

print("playlists:")
for playlist in lib.playlists:
    print(playlist)


print("playlist items:")
for playlist in lib.playlists:
    print(playlist)
    for item in playlist.items:
        artist = item.artist if item.artist else ''
        album  = item.album  if item.album  else ''
        track  = item.title  if item.title  else ''
        date_added = item.getItunesAttribute('Date Added')
        year = item.getItunesAttribute('Year')
        genre = item.getItunesAttribute('Genre')
        print("{}\t{}\t{}\t{}\t{}\t{}".format(track,artist,album,year,date_added,genre))
    print('')
