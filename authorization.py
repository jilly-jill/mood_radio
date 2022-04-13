
"""
API Access Keys
"""
import requests

CLIENT_ID = "CLIENT_ID",
CLIENT_SECRET = "CLIENT_SECRET"

AUTH_URL = 'https://accounts.spotify.com/api/token'

response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': '707aea154a924b8889b0a3dfccbc64d3',
    'client_secret': 'ce5f3cab4af34242adc6ceb3e4627a1a',
})

auth_response_data = response.json()

access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

print(headers)
