"""
#GET Request & JSON Modification
"""
from itertools import count

import requests
import authorization
import pandas as pd

class refData:
    def __init__(self, artist, album, track):
        self.artist = artist
        self.album = album
        self.track = track

# called in main creates welcome header and prompt for user info

API_SEARCH = 'https://api.spotify.com/v1/'

def welcome():
    print("\nGENERIC WELCOME MESSAGE\n")
    name = input("Before we begin, just who am I speaking to?:\n> ").capitalize()
    return name


def search_artist(link, artist):
    data = requests.get(f"{link}search?q={artist}&type=artist", headers=authorization.headers)
    data = data.json()
    artist_id = data['artists'].get('items')[0].get('id')
    return artist_id


def search_artist_album_id(API_SEARCH, artist_id, album_ids):
    artist_albums = API_SEARCH + 'artists/' + artist_id + '/albums'
    album_request = requests.get(artist_albums, headers=authorization.headers, params = {'include_groups': 'album'})
    album_request = album_request.json()
    album_ids = []
    requested = album_request['items']
    print(f'requested: {requested}')
    for al in requested:
        album_ids.append(al['id'])
        print(album_ids)
    return album_ids

def search_artist_album_names(API_SEARCH, artist_id, album_names):
    artist_albums = API_SEARCH + 'artists/' + artist_id + '/albums'
    album_request = requests.get(artist_albums, headers = authorization.headers, params = {'include_groups': 'album'})
    album_request = album_request.json()
    requested = album_request ['items']
    print(f'requested: {requested}')
    for al in requested:
        album_names.append(al['name'])
        print(album_names)
    return album_names

def search_artist_album_release(API_SEARCH, artist_id, album_release):
    artist_albums = API_SEARCH + 'artists/' + artist_id + '/albums'
    album_request = requests.get(artist_albums, headers = authorization.headers, params = {'include_groups': 'album'})
    album_request = album_request.json()
    requested = album_request ['items']
    print(f'requested: {requested}')
    for al in requested:
        album_release.append(al['release_date'])
        print(album_release)
    return album_release

def pull_all_tracks(API_SEARCH, ids, mood):
    track_ids = []
    for i in ids:
        api_url = API_SEARCH + 'albums/' + i + '/tracks'
        track_list = requests.get(api_url, headers = authorization.headers)
        tracks_list = track_list.json()
        for track in tracks_list.get('items'):
            track_ids.append(track.get('id')),
            mood.append(track.get('name')),
    print(f'track-list: {tracks_list}')
    print(f'mood: {mood}')
    print(f'track-ids: {track_ids}')
    return track_list and track_ids

def pull_audio_analysis(API_SEARCH, track_id, mood):
    for tk in track_id:
        API_AUDIO = f'{API_SEARCH}audio-features/{track_id}'
        audio_analysis = requests.get(API_AUDIO, headers = authorization.headers)
        audio_analysis = audio_analysis.json()
        mood.insert(0, track_id)
        mood.insert(1, audio_analysis.get('danceability')),
        mood.insert(2, audio_analysis.get('valence')),
        mood.insert(3, audio_analysis.get('energy')),
        mood.insert(4, audio_analysis.get('mode')),
        mood.insert(5, audio_analysis.get('tempo'))


    # def get_metrics()


albums = []
analyzed_data = []
feel = []
artist_id = ""


def main():
    name = welcome()
    artist = input(f"And what artist are we looking into today, {name}?:\n> ").lower()
    artist_id= search_artist(API_SEARCH, artist)
    album_ids = []
    album_names = []
    album_date = []
    album_ids = search_artist_album_id(API_SEARCH, artist_id, album_ids)
    album_names = search_artist_album_names(API_SEARCH, artist_id, album_names)
    album_date = search_artist_album_release(API_SEARCH, artist_id, album_date)
    usr_album = []
    def build_list(usr_album, album_ids, album_date):
        usr_album.append(album_names)
        usr_album.append(album_date)
        usr_album.append(album_ids)
        return usr_album
    usr_album = build_list(usr_album, album_ids, album_date)
    print(usr_album)
    def len_elem(usr_album, album_names):
        element = 0
        for element in usr_album:
            element = (f"{element}" + 1)
        idx = 0
        for idx in album_names:
            idx = (f"{idx}" + 1)
        return element and idx
    element = len_elem(usr_album, album_names)
    idx = len_elem(usr_album, album_names)
    format_itm = (usr_album[element][idx].pop())
    print(format_itm)
    # usr_alb_pref = input(f'Which of the following albums is your favorite?: {album_na(album_names)}\n> ')
    # turn usr_alb_pref
    # na = print(album_na(album_names))






            #usr_album.insert(length, album_date)
            # for i in usr_album:
            #     length = usr_album.index(i)
            #     usr_album.insert(length, album_ids)
            #     return usr_album
    usr_album = build_list(usr_album, album_ids, album_date)


    # return length
    #
    # # insert_date = usr_album.insert(length_album - 1, album_date)
    # # insert_id = usr_album.insert(length_album + insert_date, album_ids)
    # # print(f'{usr_album}', {insert_id}, {insert_date})
    # # print(f'USR_ALBUM: {usr_album}')
    # mood = []
    # parsed_data = {}
    # for i in album_date:
    #     parsed_data.update({i: ""})
    #     return parsed_data
    # track_ids = pull_all_tracks(API_SEARCH, album_ids, mood)
    # mood = mood
    # pull_audio_analysis(API_SEARCH, track_ids, mood)
    # print(mood)


# def switch_case(clean_list):
#     for clean in clean_list:
#         clean = float(clean)
#         if (clean[0]) >= 0.5:
#             True
#         if (clean[1]) >= 0.4:
#             True
#         if (clean[2]) >= 0.5:
#             True
#         if (clean[3]) == 1.0:
#             True
#         if (clean_list[4]) >= 95:
#             True
#         else:
#             return False
#         if True:
#             clean_lit.append('Uptempo')
    #     if get_item >= 0.2:
    # elif 0.2 <= get_item <= 0.5 and 0.4 <= get_item <= 0.6 and 0.4 <= get_item <= 0.65 and get_item <= 105 and get_item >= 85:
    #     mood_class = 'Mellow'
    #     status.append(mood_class)

#     'release_date': f'{release_date}',
#     'song_title': f'{track_art}',
#     'album_title': f'{album_name_store}',
#     'album_id': f'{id_store}',
#     'artist_id': f'{artist_id}',
#     'song_id': f'{track_id}',
#     'danceability': f'{audio_analysis["danceability"]}',
#     'valence': f'{audio_analysis["valence"]}',
#     'energy': f'{audio_analysis["energy"]}',
#     'mode': f'{audio_analysis["mode"]}',
#     'tempo': f'{audio_analysis["tempo"]}',
# })

#
# for stat in clean_list:
#     if clean_list[0] >= 0.5 and stat[1] >= 0.5 and stat[2] >= 0.6 and stat[3] == 1 and stat[4] >= 110.0:
#         mood_class = 'Upbeat'
#         clean_list.append(mood_class)
#     elif 0.2 <= stat[0] <= 0.5 and 0.4 <= stat[1] <= 0.6 and 0.4 <= stat[2] <= 0.65 and stat[
#     4] <= 105 and stat[4] >= 85:
#         mood_class = 'Mellow'
#         status.append(mood_class)


# elif v <= 0.20 and d <= 0.3 and e <= 0.3 and m == 0 and t <= 80.0:
#     mood.append('Melancholy')
# elif v >= 0.8 and d >= 0.8 and t >= 120.0:
#     mood.append('Intense')


# upbeat
# if valence >= 0.70 danceability >= 0.8 & energy > 0.6 & mode == 1 & tempo => 120.0

# melancholy
# if valence =< 0.20 danceability >= 0.3 & energy <= 0.2 mode == 0 & tempo <= 85

# mellow
# if valence >= 0.50 danceability <= 0.6 & >= 0.3 energy <= 0.8 & >= 0.4 temp >= 70 & <= 100

# intense
# if danceability >= .8 energy >= .8 & temp >= 120


# audio_analysis.update({
#     'Song Title' : f'{track_art}',
#     'Album Title' : f'{album_name_store}',
#     'Album Id' : f'{id_store}',
#     'Artist Id' : f'{artist_id}',
#     'Song Id' : f'{track_id}'
# })
# print(audio_analysis.update)
# for audio in audio_analysis.get('track'):
# tempo / time_signature / key / mode / rhythm string

# track_id = track['id']
# print(track_id)
# track_name = track('name')
#     print(f"ID: {track_id}\nName: {track_name}")


# print(artist_request)
# artist_request = artist_request.json()
# print(artist_request)


# print(t)
# artists -> dictionary / items -> listitems.get('id')

if __name__ == '__main__':
        main()