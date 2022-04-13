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
API = 'https://api.spotify.com/v1/search?q={artist}'
param = '&type=artist'

# GET request with proper authorization header
r = requests.get(API + param, headers=headers)
r = r.json()
pprint(r)



