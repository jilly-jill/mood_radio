"""
#GET Request & JSON Modification
"""
from pprint import pprint
import requests
import authorization


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
API_AUDIO = 'https://api.spotify.com/v1/audio-analysis/id?q='
API_ARTIST = 'https://api.spotify.com/v1/artists/0TnOYISbd1XYRBk9myaseg'


# GET request with proper authorization header
def search_get_formatted(api_url):
    r = requests.get(api_url, headers=headers)
    r = r.json()
    return pprint(r)


get_request_formatted(API_SEARCH)

# artists -> dictionary / items -> listitems.get('id')

