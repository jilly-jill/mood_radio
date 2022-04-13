"""
#GET Request & JSON Modification
"""
from pprint import pprint
import requests
import authorization
import pandas as pd

# called in main creates welcome header and prompt for user info
def welcome():
    print("\nGENERIC WELCOME MESSAGE\n")
    name = input("Before we begin, just who am I speaking to?:\n>")
    return name


# call welcome and store name input in user variable
user = welcome()
# imported authorization headers from authorization file
headers = authorization.headers

# artist variable created by user input
artist = input('\nArtist Name:\n>').lower()

# base URL for API endpoints
API_SEARCH = f'https://api.spotify.com/v1/search?q={artist}&type=artist'



# GET request with proper authorization header
albums = []
analyzed_data = []
feel = []
artist_id = ""
data = requests.get(API_SEARCH, headers=headers)
data = data.json()
artist_id = data['artists'].get('items')[0].get('id')
artist_albums = f'https://api.spotify.com/v1/artists/{artist_id}/albums'
album_request = requests.get(artist_albums, headers=headers, params={'include_groups': 'album'})
album_request = album_request.json()
for album in album_request['items']:
    determine_mood = []
    id_store = album['id']
    album_name_store = album['name']
    determine_mood.append(album_name_store)
    release_date = album['release_date']
    determine_mood.append(release_date)
    if albums.__contains__(album_name_store):
        albums.append(album_name_store.upper())
    else:
        track_list = requests.get(f'https://api.spotify.com/v1/albums/{id_store}/tracks', headers=headers)
        tracks_list = track_list.json()
    for track in tracks_list.get('items'):
        track_id = (track.get('id'))
        track_art = track.get('name')
        determine_mood.append(track_art)
        API_AUDIO = f'https://api.spotify.com/v1/audio-features/{track_id}'
        audio_analysis = requests.get(API_AUDIO, headers=headers)
        audio_analysis = audio_analysis.json()
        mood = []
        d = mood.append(audio_analysis['danceability'])
        v = mood.append(audio_analysis['valence'])
        e = mood.append(audio_analysis['energy'])
        m = mood.append(audio_analysis['mode'])
        t = mood.append(audio_analysis['tempo'])
        determine_mood.append(mood)
        audio_analysis.update({
        'release_date': f'{release_date}',
        'song_title' : f'{track_art}',
        'album_title' : f'{album_name_store}',
        'album_id' : f'{id_store}',
        'artist_id' : f'{artist_id}',
        'song_id' : f'{track_id}',
        'danceability' : f'{audio_analysis["danceability"]}',
        'valence' : f'{audio_analysis["valence"]}',
        'energy': f'{audio_analysis["energy"]}',
        'mode': f'{audio_analysis["mode"]}',
        'tempo': f'{audio_analysis["tempo"]}',
        })
    print(determine_mood)

# if v => 0.7 and d => 0.8 and e => 0.6 and m == 1 and t => 120.0:
    #     mood.append('Upbeat')
    # elif 0.50 <= v and 0.6 >= d and 0.4 <= e and t <= 85.0:
    #     mood.append('Mellow')
    # elif v <= 0.20 and d <= 0.3 and e <= 0.3 and m == 0 and t <= 80.0:
    #     mood.append('Melancholy')
    # elif v >= 0.8 and d >= 0.8 and t >= 120.0:
    #     mood.append('Intense')
# df = pd.DataFrame(data)
# df['release_date'] = pd.to_datetime(df['release_date'])
# df = df.sort_values(by="release_date")
#
# df.head()




            #upbeat
            #if valence >= 0.70 danceability >= 0.8 & energy > 0.6 & mode == 1 & tempo => 120.0

            #melancholy
            #if valence =< 0.20 danceability >= 0.3 & energy <= 0.2 mode == 0 & tempo <= 85

            #mellow
            #if valence >= 0.50 danceability <= 0.6 & >= 0.3 energy <= 0.8 & >= 0.4 temp >= 70 & <= 100

            #intense
            #if danceability >= .8 energy >= .8 & temp >= 120





            # audio_analysis.update({
            #     'Song Title' : f'{track_art}',
            #     'Album Title' : f'{album_name_store}',
            #     'Album Id' : f'{id_store}',
            #     'Artist Id' : f'{artist_id}',
            #     'Song Id' : f'{track_id}'
            # })
        # print(audio_analysis.update)
    # for audio in audio_analysis.get('track'):
   #tempo / time_signature / key / mode / rhythm string

        # track_id = track['id']
        # print(track_id)
        # track_name = track('name')
    #     print(f"ID: {track_id}\nName: {track_name}")


    # print(artist_request)
    # artist_request = artist_request.json()
    # print(artist_request)





# print(t)
# artists -> dictionary / items -> listitems.get('id')


