
"""
API Access Keys
"""
import requests

CLIENT_ID = "CLIENT_ID",
CLIENT_SECRET = "CLIENT_SECRET"

AUTH_URL = 'https://accounts.spotify.com/api/token'

response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = response.json()

access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

print(headers)
