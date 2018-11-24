from gmusicapi import Mobileclient

api = Mobileclient()
loggedIn = api.login('soush915@gmail.com', 'Sou91599!!', '001D0904BFFA')
# '699BCB3E27263F4A'

from gmusicapi.utils import utils
with open(utils.log_filepath, 'r') as fin:
    print(fin.read())
playlists = api.get_all_user_playlist_contents()
print(playlists)


# trackInfo = api.get_track_info(trackId)
# api.get_album_info(trackInfo['albumId'])
# api.get_artist_info(trackInfo['artistId'])

# api.get_stream_url


# api.logout()


import json

with open('data.json', 'w') as fp:
    json.dump(playlists, fp)
# Debug
# from gmusicapi.utils import utils
# with open(utils.log_filepath, 'r') as fin:
#     print(fin.read())



# Expand w/ Websocketapi thing from googleplaymusic desktop client to see what I'm listening to right now (sync with it later)
